# Odoo Community: Was ist frei verfügbar?

Stand: 25.10.2026. Grundlage ist der offizielle Quellcode auf GitHub
(`github.com/odoo/odoo`), Branches 18.0, 19.0 und 20.0. Ausgewertet wurde die
Modulbeschreibung (`__manifest__.py`) jedes Moduls. Die vollständigen Listen
liegen unter [`data/`](../data/) (CSV für Excel und als Markdown).

| Version | Commit (24.10.2026) | Module ohne Tests | davon Apps | Länderpakete | optionale Erweiterungen | technische Brückenmodule |
|---|---|---|---|---|---|---|
| 20.0 (aktuell) | `0af7f93d` | 624 | 34 | 230 | 120 | 240 |
| 19.0 | `8b87b900` | 624 | 34 | 233 | 120 | 237 |
| 18.0 | `98e48692` | 610 | 35 | 234 | 98 | 243 |

**Alle Module der Community Edition stehen unter LGPL-3** (laut Manifest jedes
einzelnen Moduls). Sie dürfen kopiert, verändert und intern ohne Lizenzkosten
betrieben werden.

Begriffe:

- **App**: eigene Anwendung mit Menü (z. B. CRM, Lager).
- **Erweiterung**: optional zuschaltbare Funktion (z. B. Lohnfertigung).
- **Technisches Brückenmodul**: verbindet zwei Apps und wird automatisch
  mitinstalliert (z. B. `sale_stock` verbindet Verkauf und Lager).
- **Länderpaket**: Kontenrahmen, Steuern, Belegformate eines Landes.

---

## 1. Die 34 Apps der Community Edition (Odoo 20.0)

| Bereich | App (technischer Name) | Inhalt |
|---|---|---|
| **Vertrieb** | CRM (`crm`) | Leads, Verkaufschancen, Pipeline |
| | Verkauf (`sale_management`) | Angebot, Auftrag, Rechnung, Preislisten, Varianten |
| | Kontakte (`contacts`) | Zentrales Adressbuch |
| | Kassensystem (`point_of_sale`) | Ladenkasse, Zahlungen |
| | Restaurant (`pos_restaurant`) | Gastronomie-Erweiterung der Kasse |
| **Finanzen** | Rechnungsstellung (`account`) | Ausgangs- und Eingangsrechnungen, Zahlungen, Buchungsjournale, Steuern |
| | Spesen (`hr_expense`) | Auslagen erfassen, freigeben, weiterberechnen |
| **Lieferkette** | Lager (`stock`) | Lagerorte, Wareneingang/-ausgang, Los- und Seriennummern, Inventur, Routen |
| | Fertigung (`mrp`) | Stücklisten, Fertigungsaufträge, Arbeitsplätze |
| | Einkauf (`purchase`) | Bestellungen, Ausschreibungen, Rahmenverträge |
| | Reparaturen (`repair`) | Reparaturaufträge |
| | Wartung (`maintenance`) | Anlagen und Wartungsanfragen |
| **Projekte** | Projekt (`project`) | Aufgaben, Phasen, Zusammenarbeit |
| **Kommunikation** | Discuss (`mail`) | Chat, Kanäle, E-Mail-Gateway (E-Mails direkt am Datensatz) |
| | Kalender (`calendar`) | Termine, Besprechungen |
| | To-Do (`project_todo`) | Notizen und Aufgabenlisten |
| | Live-Chat (`im_livechat`) | Chat mit Website-Besuchern |
| | Datenbereinigung (`data_recycle`) | Alte Datensätze finden und archivieren |
| **Website & Marketing** | Website (`website`) | Website-Baukasten |
| | eCommerce (`website_sale`) | Onlineshop |
| | eLearning (`website_slides`) | Schulungsplattform |
| | Online-Stellen (`website_hr_recruitment`) | Stellenanzeigen |
| | E-Mail-Marketing (`mass_mailing`) | Newsletter, Kampagnen |
| | SMS-Marketing (`mass_mailing_sms`) | SMS-Kampagnen |
| | Veranstaltungen (`website_event`) | Events, Ticketverkauf |
| | Umfragen (`survey`) | Fragebögen, Live-Umfragen |
| | Marketing-Karten (`marketing_card`) | Teilbare Werbegrafiken |
| **Personal** | Mitarbeiter (`hr`) | Personalstamm |
| | Anwesenheiten (`hr_attendance`) | Kommen/Gehen |
| | Abwesenheiten (`hr_holidays`) | Urlaub, Krankheit |
| | Bewerbermanagement (`hr_recruitment`) | Bewerbungsprozess |
| | Kompetenzen (`hr_skills`) | Qualifikationen, Lebenslauf |
| | Fuhrpark (`fleet`) | Fahrzeuge und Kosten |
| | Mittagessen (`lunch`) | Essensbestellung |

Unterschied zu 18.0: Dort gibt es zusätzlich die App „Arbeitsverträge“
(`hr_contract`). Ab 19.0 ist sie keine eigene App mehr.

## 2. Wichtige Erweiterungen in der Community Edition

Diese Funktionen sind frei enthalten und für einen Hersteller wie MESSOTRON
besonders relevant:

| Bereich | Module | Funktion |
|---|---|---|
| Lager & Fertigung | `stock_account`, `mrp_account` | Bestandsbewertung, Kostenrechnung Fertigung |
| | `stock_landed_costs` | Anschaffungsnebenkosten (Fracht, Zoll) auf Ware verteilen |
| | `mrp_subcontracting` | Lohnfertigung |
| | `stock_dropshipping` | Streckengeschäft |
| | `product_expiry` | Haltbarkeits-/Ablaufdaten |
| | `mrp_repair`, `sale_mrp`, `purchase_mrp` | Verknüpfung Fertigung mit Reparatur, Verkauf, Einkauf |
| Verkauf & Einkauf | `purchase_requisition` | Rahmenverträge, Ausschreibungen |
| | `delivery`, `stock_delivery` | Versandarten mit Preisregeln (ohne Anbindung an Versanddienstleister) |
| | `loyalty`, `sale_loyalty` | Rabatte, Gutscheine, Treueprogramme |
| | `payment_stripe`, `payment_paypal`, `payment_mollie`, `payment_adyen` | Zahlungsanbieter für Shop und Rechnungen |
| Projekte | `hr_timesheet`, `sale_timesheet` | Zeiterfassung auf Aufgaben, Abrechnung nach Aufwand |
| | `sale_project`, `project_purchase`, `project_mrp` | Projekte aus Aufträgen, Kosten aus Einkauf und Fertigung |
| Deutschland | `l10n_de` | Kontenrahmen SKR03/SKR04, DATEV-Steuerschlüssel an den Steuern, GoBD-Protokollierung standardmäßig aktiv |
| | `l10n_din5008` (+ `_sale`, `_purchase`, `_stock`, `_repair`, `_expense`) | Belege im Format DIN 5008 |
| | `account_edi_ubl_cii` | E-Rechnung: **XRechnung** (UBL) und **ZUGFeRD/Factur-X** (CII), Import und Export |
| | `account_peppol` | Versand und Empfang über das Peppol-Netz |
| | `l10n_eu_oss` | EU-One-Stop-Shop (Fernverkauf an Privatkunden in der EU) |
| Kommunikation | `google_gmail`, `microsoft_outlook` | E-Mail-Postfächer von Google/Microsoft 365 anbinden |
| | `google_calendar`, `microsoft_calendar` | Kalender synchronisieren |
| | `portal` | Kundenportal (Angebote, Rechnungen, Lieferungen online einsehen) |
| | `sms` | SMS-Versand |
| Auswertung & Automatisierung | `spreadsheet_dashboard` | Dashboards (Anzeige; Bearbeitung als Tabelle ist Enterprise) |
| | `base_automation` | Automatisierungsregeln ohne Programmierung |

## 3. Was nur die Enterprise Edition hat

Belegt aus zwei Quellen:

- **Odoo-Code selbst**: Der Community-Code enthält Platzhalter für
  Enterprise-Apps (`to_buy` in `odoo/addons/base/data/ir_module_module.xml`) und
  Schalter mit Upgrade-Hinweis in den Einstellungen (`widget="upgrade_boolean"`).
  Liste: [`data/odoo-20.0/enterprise_referenced.csv`](../data/odoo-20.0/enterprise_referenced.csv).
- **Editionsvergleich auf odoo.com**: Apps, die dort aufgeführt sind, im
  Community-Code aber nicht vorkommen.

Freie Alternativen stammen aus der **OCA** (Odoo Community Association, siehe
Abschnitt 4). Mit „geprüft“ markierte Module habe ich im jeweiligen
OCA-Repository für Version 18.0 nachgesehen. Bei „zu prüfen“ steht die
Prüfung noch aus.

| Enterprise-Funktion | technischer Name | Freie Alternative |
|---|---|---|
| **Vollständige Buchhaltung**: Bilanz, GuV, Hauptbuch, OP-Listen | `accountant`, `account_reports` | `account_financial_report`, `mis_builder` (geprüft) |
| **BWA / Managementberichte** | `account_reports` | `l10n_de_mis_reports` + `mis_builder` (geprüft) |
| **Bankabgleich-Oberfläche** | `accountant` | `account_reconcile_oca` (geprüft) |
| **Bankauszug-Import CAMT/CSV/OFX** | `account_bank_statement_import_camt` u. a. | `account_statement_import_camt` (geprüft) |
| **DATEV-Export** (Community hat nur die Steuerschlüssel) | – | `datev_export_dtvf`, `datev_export_xml` (geprüft) |
| **Umsatzsteuer-Voranmeldung / ZM** | `account_reports` | `l10n_de_tax_statement`, `l10n_de_tax_statement_zm` (geprüft) |
| SEPA-Lastschrift, SEPA-Überweisungsdateien | `account_sepa_direct_debit`, `account_iso20022` | OCA „bank-payment“ (zu prüfen) |
| Budgets, Wechselkurse automatisch | `account_budget`, `currency_rate_live` | zu prüfen |
| Belegerkennung (OCR) für Eingangsrechnungen | `account_extract` | zu prüfen |
| **Barcode-App für Lager** | `stock_barcode` | `stock_barcodes` (geprüft) |
| **Versandanbindung** DHL, UPS, FedEx, Sendcloud | `delivery_dhl`, `delivery_ups`, `delivery_sendcloud` u. a. | `delivery_sendcloud_oca`, `delivery_ups_oca`, `delivery_roulier`, `delivery_dachser`, `delivery_schenker` (geprüft) |
| **Qualität** (Prüfpunkte, Qualitätsmeldungen) | `quality_control` | zu prüfen |
| **PLM** (Änderungsaufträge, Stücklisten-Versionen) | `mrp_plm` | zu prüfen |
| **MRP II** (Werkerterminal, Arbeitsplanung) | `mrp_workorder` | zu prüfen |
| Produktionsprogrammplanung (MPS) | `mrp_mps` | zu prüfen |
| **Helpdesk** (Tickets, SLA) | `helpdesk` | `helpdesk_mgmt` und rund 30 Ergänzungen (geprüft) |
| **Dokumentenverwaltung** | `documents` | `dms` (geprüft) |
| **Studio** (Anpassen ohne Code) | `web_studio` | entfällt: Anpassungen direkt als eigene Module |
| Zeiterfassung mit Raster, Timer, Freigabe | `timesheet_grid` | Basis in Community (`hr_timesheet`), Rest zu prüfen |
| Planung, Termine, Außendienst | `planning`, `appointment`, `industry_fsm` | zu prüfen |
| Sign, Knowledge, Freigaben, VoIP | `sign`, `knowledge`, `approvals`, `voip` | zu prüfen |
| Abonnements, Vermietung, Amazon-Connector | `sale_subscription`, `sale_renting`, `sale_amazon` | zu prüfen |
| Lohnabrechnung, Mitarbeiterbeurteilung, Empfehlungen | `hr_payroll`, `hr_appraisal`, `hr_referral` | in DE meist ohnehin extern (DATEV Lohn) |
| Marketing-Automation, Social Marketing | `marketing_automation`, `social` | zu prüfen |
| Mobile Apps (iOS/Android), IoT, Tabellen bearbeiten | `web_mobile`, `iot`, `spreadsheet_edition` | Weboberfläche ist mobil nutzbar; Rest zu prüfen |

## 4. OCA: Wie weit sind die freien Ergänzungen je Version?

Die OCA ist ein Verein, der für jede Odoo-Version freie Module pflegt. Neue
Versionen werden nach und nach portiert. Gezählt sind die Module je Branch
(Stand 25.10.2026):

| OCA-Repository | Inhalt | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| `l10n-germany` | DATEV-Export, UStVA, BWA-Vorlagen | 7 | **14** | 7 | 0 |
| `account-financial-reporting` | Bilanz, GuV, Hauptbuch, OP-Listen | 9 | 8 | 5 | 0 |
| `mis-builder` | Kennzahlen- und Managementberichte | 3 | 3 | 3 | 3 |
| `account-reconcile` | Bankabgleich | 7 | **19** | 4 | 0 |
| `bank-statement-import` | Bankauszug-Import (CAMT u. a.) | 16 | **20** | 15 | 0 |
| `delivery-carrier` | Versanddienstleister | 35 | **62** | 25 | 0 |
| `stock-logistics-barcode` | Barcode im Lager | 5 | 7 | 3 | 0 |
| `helpdesk` | Helpdesk | 25 | **32** | 17 | 0 |
| `dms` | Dokumentenverwaltung | 4 | 7 | 1 | 0 |
| `OpenUpgrade` | Datenbank-Migration zwischen Versionen | ✓ | ✓ | ✓ | noch leer |

**Folgerung:** Odoo 20.0 ist gerade erst erschienen. Fast alle OCA-Module gibt
es bisher nur bis 19.0, am vollständigsten für 18.0. Wer heute mit Community
und OCA produktiv gehen will, hat mit 18.0 die reifste Basis. Odoo pflegt
allerdings nur die drei jeweils neuesten Hauptversionen. 18.0 fällt also mit
dem Erscheinen von 21.0 (voraussichtlich Herbst 2027) aus der Pflege. 19.0 ist
der bessere Startpunkt, sobald die benötigten OCA-Module dort verfügbar sind.

## 5. Lizenzen im Überblick (keine Rechtsberatung)

- **Odoo Community: LGPL-3.** Interne Nutzung und Anpassung sind frei. Eigene
  Zusatzmodule dürfen proprietär bleiben. Pflichten entstehen erst bei
  Weitergabe veränderten Odoo-Codes.
- **OCA: überwiegend AGPL-3**, einzelne Module LGPL-3 (z. B. `dms`,
  `delivery_sendcloud_oca`). Intern unproblematisch. Wer ein AGPL-Modul
  *verändert* und Dritte es über das Netz nutzen (Kundenportal, Webshop), muss
  ihnen den veränderten Quelltext anbieten. Deshalb eigene Anpassungen in
  eigenen Modulen halten, nicht in OCA-Modulen.
- **Enterprise: OEEL-1**, proprietär. Code nicht kopieren.
- **Marke:** Ein eigenes System darf nicht „Odoo“ heißen.

## 6. Daten aktualisieren

```bash
# Nur die Modulbeschreibungen laden (wenige MB statt mehrerer GB)
git clone --depth 1 --filter=blob:none --no-checkout --branch 20.0 \
    https://github.com/odoo/odoo /pfad/odoo-20.0
cd /pfad/odoo-20.0
git sparse-checkout set --no-cone '/addons/*/__manifest__.py' \
    '/odoo/addons/*/__manifest__.py' '/odoo/release.py' \
    '/odoo/addons/base/data/ir_module_module.xml'
git ls-tree -r --name-only HEAD | grep -E '(^|/)views/.*(res_config|settings).*\.xml$' \
    | grep -v '/tests/' | sed 's#^#/#' | git sparse-checkout add --no-cone --stdin
git checkout 20.0

# Auswertung
python3 -I scripts/odoo_module_inventory.py /pfad/odoo-20.0 --out data/odoo-20.0
```
