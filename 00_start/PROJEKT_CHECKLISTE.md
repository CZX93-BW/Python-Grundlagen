# Checkliste für dein nächstes Python-Projekt

[Zum Leitfaden](PROJEKTLEITFADEN.md)

## Start

- [ ] Zweck, Eingaben, Ausgaben und Fertig-Kriterien sind notiert.
- [ ] Projektumfang und zunächst ausgelassene Funktionen sind klar.
- [ ] Python-Version und Startordner sind festgelegt.
- [ ] Eigene virtuelle Umgebung angelegt und in VS Code ausgewählt.
- [ ] Die Struktur passt zur tatsächlichen Größe des Projekts.

## Umsetzung

- [ ] Namen erklären Bedeutung und bei Bedarf Einheiten.
- [ ] Funktionen haben einen klaren Vertrag und überschaubare Verantwortung.
- [ ] Ein-/Ausgabe ist von wiederverwendbarer Logik getrennt.
- [ ] Eingaben an Systemgrenzen werden fachlich und technisch geprüft.
- [ ] Rückgabewerte und mögliche Fehler sind eindeutig.
- [ ] Veränderbare Standardargumente und unbeabsichtigte gemeinsame Daten sind vermieden.
- [ ] Ressourcen werden geordnet geschlossen.
- [ ] Fehler werden verständlich behandelt und nicht verschluckt.

## Prüfung

- [ ] Normalfälle und relevante Grenzen sind getestet.
- [ ] Ein gefundener wichtiger Fehler hat einen gezielten Regressionstest.
- [ ] Tests verwenden keine persönlichen Daten oder echten externen Schreibaktionen.
- [ ] Linter, Formatprüfung, Typprüfung und Tests sind ausgeführt; Einschränkungen dokumentiert.
- [ ] Abhängigkeiten sind bewusst gewählt und der geprüfte Stand ist festgehalten.
- [ ] Einrichtung und Start wurden in einer frischen Umgebung nachvollzogen.
- [ ] Falls mehrere Python-/Betriebssystemversionen versprochen werden, wurden sie geprüft.

## Weitergeben

- [ ] README erklärt Einrichtung, Start, Konfiguration, Tests und Grenzen.
- [ ] Beispielkonfiguration enthält keine echten Zugangsdaten.
- [ ] Versionsverwaltung enthält keine .venv, Caches oder Geheimnisse.
- [ ] Der Diff enthält nur beabsichtigte Änderungen.
- [ ] Falls ein Paket verteilt wird: gebautes Paket separat installiert und gestartet.
- [ ] Falls veröffentlicht wird: Metadaten, Paketinhalt und Lizenz bewusst geprüft.
- [ ] Für produktive Daten sind Backup und Wiederherstellung geklärt.
