# Einschätzung: Eigenes ERP auf Basis von Odoo Community

Stand: 25.10.2026

## These

> Wenn man an den Community-Code anknüpft, kann man mit der Zeit ein gut
> ausgebautes eigenes ERP betreiben, mit Funktionen, die genau auf den eigenen
> Bedarf zugeschnitten sind. Mit Hilfe von KI ist das für einen Entwickler
> machbar.

## Bewertung

**Die These ist tragfähig, wenn auf Odoo aufgebaut statt neu geschrieben
wird.** Odoo ist ein Baukasten. Das Framework übernimmt Datenbank, Oberfläche,
Rechte, Mehrmandantenfähigkeit, Workflows, E-Mail-Anbindung und Berichte.
Eigene Funktionen entstehen als eigene Module, die den Standard erweitern,
ohne ihn zu verändern. Genau für diese Art Arbeit ist KI-gestützte Entwicklung
gut geeignet: Odoo-Code ist sehr einheitlich aufgebaut, gut dokumentiert und
öffentlich einsehbar.

Der Aufwand liegt weniger im Bauen neuer Funktionen als in vier Daueraufgaben:

### 1. Jährliche Versionssprünge

Odoo erscheint jedes Jahr in einer neuen Hauptversion und pflegt nur die drei
neuesten. Dabei baut Odoo auch den Standard um. Belege aus dem Quellcode:

- Von 19.0 auf 20.0 sind 34 Module neu hinzugekommen, 30 sind entfallen oder
  in andere Module aufgegangen (z. B. `stock_picking_batch`, `base_vat`,
  `website_sale_wishlist`). Länderpakete und Testmodule sind dabei nicht
  mitgezählt.
- Das Modul für Arbeitsverträge (`hr_contract`) gibt es ab 19.0 nicht mehr.

Jedes eigene Modul und die Datenbank müssen deshalb etwa alle ein bis zwei
Jahre migriert werden. Für Community-Datenbanken gibt es dafür das freie
Werkzeug OpenUpgrade. Mit KI-Unterstützung und automatischen Tests ist das gut
beherrschbar, aber es ist fest einzuplanen.

### 2. Buchhaltung und Compliance

GoBD, Verfahrensdokumentation, DATEV-Übergabe an den Steuerberater,
E-Rechnung und Umsatzsteuer-Voranmeldung sind Pflicht und ändern sich
regelmäßig. Das sollte man nicht selbst bauen. Stattdessen den Odoo-Standard
plus die gepflegten OCA-Module nutzen (siehe
[01-odoo-community-module.md](01-odoo-community-module.md), Abschnitt 3) und
mit dem Steuerberater abstimmen.

### 3. Betrieb

Server, tägliche Backups mit Rücksicherungstest, Sicherheitsupdates,
Überwachung, zuverlässiger E-Mail-Versand. Das lässt sich gut automatisieren
(Docker, Skripte), muss aber jemand verantworten.

### 4. Abhängigkeit von einer Person

Wenn nur eine Person das System versteht, ist das ein Betriebsrisiko. Dagegen
helfen: alles in diesem Repository, nachvollziehbare Commits, automatische
Tests und Dokumentation.

## Leitlinien für dieses Repository

1. **Odoo-Kern nie verändern.** Kein Fork. Alle Anpassungen als eigene Module
   unter `addons/` mit Präfix `messotron_`. Nur so bleiben Updates und
   Versionssprünge machbar.
2. **Standard vor OCA vor Eigenbau.** Erst prüfen, ob Odoo oder die OCA die
   Funktion schon hat.
3. **Jede Anpassung mit Tests.** Odoo bringt ein Testframework mit; Tests sind
   die Absicherung für jeden Versionssprung.
4. **Eine Zielversion festlegen und den Upgrade-Rhythmus planen.**

## Nächste Schritte

1. **Ist-Aufnahme:** Welche Odoo-Version und Edition, welches Hosting (Odoo
   Online, Odoo.sh, eigener Server), welche Apps und welche
   Enterprise-Funktionen werden tatsächlich genutzt?
2. **Lückenanalyse:** Für jede genutzte Enterprise-Funktion den Ersatz aus
   Community oder OCA prüfen, oder den Eigenbau bewerten.
3. **Testumgebung:** Odoo Community mit OCA-Modulen per Docker aufsetzen und
   mit einer Kopie der echten Daten testen.
4. **Pilot:** Erste eigene Module für MESSOTRON-spezifische Abläufe, z. B.
   Kalibrierzertifikate, Seriennummern-Rückverfolgung, Prüfprotokolle.
