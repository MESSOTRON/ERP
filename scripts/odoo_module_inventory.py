#!/usr/bin/env python3
"""Erstellt ein Inventar aller Module eines Odoo-Community-Quellbaums.

Liest jede ``__manifest__.py`` (nur als Daten, ohne sie auszuführen) sowie
die Hinweise auf Enterprise-Module, die Odoo selbst im Community-Code
hinterlegt, und schreibt CSV-/JSON-Dateien und eine Markdown-Liste.

Aufruf:
    python3 -I scripts/odoo_module_inventory.py <odoo-quellcode> --out <zielordner>

Der Quellbaum muss mindestens enthalten:
    addons/*/__manifest__.py
    odoo/addons/*/__manifest__.py
    odoo/release.py
    odoo/addons/base/data/ir_module_module.xml
    */views/*res_config_settings*.xml   (für die Enterprise-Schalter)
"""

import argparse
import ast
import csv
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

FIELDS = [
    "technical_name", "name", "type", "category", "summary", "application",
    "auto_install", "license", "countries", "depends", "location",
]

UPGRADE_TOGGLE = re.compile(
    r'<field\s+name="module_([a-z0-9_]+)"[^>]*widget="upgrade_boolean"'
    r'|<field[^>]*widget="upgrade_boolean"[^>]*name="module_([a-z0-9_]+)"'
)


def read_version(src: Path) -> str:
    text = (src / "odoo" / "release.py").read_text(encoding="utf-8")
    match = re.search(r"^version_info\s*=\s*\((\d+),\s*(\d+)", text, re.M)
    return f"{match.group(1)}.{match.group(2)}" if match else "unbekannt"


def read_manifest(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Dict):
            return ast.literal_eval(node.value)
    raise ValueError(f"Kein Manifest-Dictionary in {path}")


def classify(tech: str, manifest: dict) -> str:
    category = manifest.get("category", "") or ""
    if tech.startswith("test_") or category.startswith("Hidden/Tests"):
        return "Test"
    if manifest.get("application"):
        return "App"
    if tech.startswith("l10n_"):
        return "Lokalisierung"
    if manifest.get("auto_install") or category.startswith(("Hidden", "Technical")):
        return "Technisch/Brücke"
    return "Erweiterung"


def collect_modules(src: Path) -> list[dict]:
    modules = []
    for location in ("odoo/addons", "addons"):
        for manifest_path in sorted((src / location).glob("*/__manifest__.py")):
            tech = manifest_path.parent.name
            manifest = read_manifest(manifest_path)
            auto_install = manifest.get("auto_install", False)
            modules.append({
                "technical_name": tech,
                "name": manifest.get("name", tech),
                "type": classify(tech, manifest),
                "category": manifest.get("category", "Uncategorized"),
                "summary": " ".join((manifest.get("summary") or "").split()),
                "application": bool(manifest.get("application", False)),
                "auto_install": bool(auto_install),
                "license": manifest.get("license", "LGPL-3"),
                "countries": ",".join(manifest.get("countries", [])),
                "depends": ",".join(manifest.get("depends", [])),
                "location": location,
            })
    return modules


def collect_enterprise(src: Path, community: set[str]) -> list[dict]:
    """Enterprise-Module, auf die der Community-Code selbst verweist."""
    found = {}
    stub_file = src / "odoo/addons/base/data/ir_module_module.xml"
    for record in ET.parse(stub_file).getroot().iter("record"):
        values = {f.get("name"): (f.text or "").strip() for f in record.iter("field")}
        if values.get("name") and record.find("field[@name='to_buy']") is not None:
            found[values["name"]] = {
                "technical_name": values["name"],
                "name": values.get("shortdesc", ""),
                "summary": values.get("summary", ""),
                "license": values.get("license", ""),
                "source": "App im Apps-Menü (to_buy)",
                "referenced_in": "odoo/addons/base/data/ir_module_module.xml",
            }
    for view in sorted(src.glob("**/views/*.xml")):
        for match in UPGRADE_TOGGLE.finditer(view.read_text(encoding="utf-8")):
            tech = match.group(1) or match.group(2)
            if tech in community or tech in found:
                continue
            found[tech] = {
                "technical_name": tech,
                "name": "",
                "summary": "",
                "license": "OEEL-1",
                "source": "Enterprise-Schalter in Einstellungen (upgrade_boolean)",
                "referenced_in": str(view.relative_to(src)),
            }
    return sorted(found.values(), key=lambda m: m["technical_name"])


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, version: str, modules: list[dict]) -> None:
    by_area = defaultdict(list)
    for module in modules:
        if module["type"] == "Test":
            continue
        area = module["category"].split("/")[0]
        if module["type"] == "Lokalisierung":
            area = "Lokalisierung (Länder)"
        by_area[area].append(module)

    lines = [
        f"# Odoo {version} Community – vollständige Modulliste",
        "",
        "Automatisch erzeugt mit `scripts/odoo_module_inventory.py` aus dem offiziellen",
        f"Quellcode (github.com/odoo/odoo, Branch {version}). Testmodule sind ausgelassen.",
        "",
        "Typ: **App** = eigene Anwendung im Apps-Menü; **Erweiterung** = optional",
        "installierbar; **Technisch/Brücke** = wird automatisch mitinstalliert, sobald",
        "die abhängigen Apps installiert sind; **Lokalisierung** = Länderpaket.",
        "",
    ]
    for area in sorted(by_area):
        entries = sorted(by_area[area], key=lambda m: (m["type"] != "App", m["technical_name"]))
        lines += [f"## {area} ({len(entries)})", "",
                  "| Technischer Name | Name | Typ | Kategorie | Kurzbeschreibung |",
                  "|---|---|---|---|---|"]
        for m in entries:
            lines.append(
                f"| `{m['technical_name']}` | {md_cell(m['name'])} | {m['type']} "
                f"| {md_cell(m['category'])} | {md_cell(m['summary'])} |"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="Pfad zum Odoo-Quellcode")
    parser.add_argument("--out", type=Path, required=True, help="Zielordner")
    args = parser.parse_args()

    version = read_version(args.source)
    modules = collect_modules(args.source)
    enterprise = collect_enterprise(args.source, {m["technical_name"] for m in modules})

    args.out.mkdir(parents=True, exist_ok=True)
    write_csv(args.out / "community_modules.csv", modules, FIELDS)
    write_csv(args.out / "enterprise_referenced.csv", enterprise,
              ["technical_name", "name", "summary", "license", "source", "referenced_in"])
    (args.out / "community_modules.json").write_text(
        json.dumps({"version": version, "modules": modules}, indent=1, ensure_ascii=False),
        encoding="utf-8")
    write_markdown(args.out / "community_modules.md", version, modules)

    counts = defaultdict(int)
    for module in modules:
        counts[module["type"]] += 1
    print(f"Odoo {version}: {len(modules)} Module", dict(sorted(counts.items())))
    print(f"Enterprise-Verweise: {len(enterprise)}")


if __name__ == "__main__":
    main()
