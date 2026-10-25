# MESSOTRON ERP

Aufbau eines eigenen ERP-Systems auf Basis von **Odoo Community** (Open Source,
LGPL-3), erweitert um freie Module der OCA und eigene Module für die Abläufe
von MESSOTRON.

## Inhalt

| Pfad | Inhalt |
|---|---|
| [`docs/01-odoo-community-module.md`](docs/01-odoo-community-module.md) | Welche Module frei verfügbar sind, was nur Enterprise hat, freie Alternativen, Reifegrad je Version |
| [`docs/02-einschaetzung-eigenes-erp.md`](docs/02-einschaetzung-eigenes-erp.md) | Machbarkeit, Risiken, Leitlinien, nächste Schritte |
| [`docs/03-vision-branchen-saas-elektrohandwerk.md`](docs/03-vision-branchen-saas-elektrohandwerk.md) | Vision: Branchen-ERP als Komplettservice (SaaS), Beispiel Elektrohandwerk – Markt, Bausteine, KI-Dienste, Architektur, Recht, Phasen |
| [`data/odoo-<version>/`](data/) | Vollständige Modullisten für Odoo 18.0, 19.0 und 20.0 (CSV, JSON, Markdown) |
| [`scripts/odoo_module_inventory.py`](scripts/odoo_module_inventory.py) | Erzeugt die Modullisten aus dem Odoo-Quellcode |

Geplant:

| Pfad | Inhalt |
|---|---|
| `addons/` | Eigene Odoo-Module (`messotron_*`) |
| `deploy/` | Docker-Setup für Test- und Produktivbetrieb |

## Kurzfassung

- Odoo 20.0 Community umfasst 624 Module (ohne Tests), darunter 34 Apps:
  CRM, Verkauf, Einkauf, Lager, Fertigung, Projekt, Rechnungsstellung,
  Discuss, Website/Shop, E-Mail-Marketing, Personal u. a.
- Für Deutschland enthalten: SKR03/SKR04, DIN 5008, XRechnung und ZUGFeRD,
  GoBD-Protokollierung.
- Nur in Enterprise: vollständige Buchhaltung mit Berichten, DATEV-Export,
  Barcode, Qualität, PLM, Helpdesk, Dokumente, Studio, Versandanbindungen u. a.
  Für viele davon gibt es freie OCA-Module, derzeit am vollständigsten für
  Version 18.0.
