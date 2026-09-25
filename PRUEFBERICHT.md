# Prüfbericht

[Start](README.md)

Stand: 25.09.2026. Prüfplattform: Linux, Python 3.12.14. Die Tests wurden mit dem erstellten Quellcode ausgeführt; Aussagen über andere Plattformen sind davon nicht automatisch abgedeckt.

| Bereich | Prüfung | Ergebnis |
| --- | --- | --- |
| Kapitelbeispiele | 90 Dateien separat gestartet, einschließlich vorbereiteter Terminaleingaben | 90/90 erfolgreich; Standardausgabe stimmt mit der Dokumentation überein |
| Musterlösungen | Dieselben verhaltensbezogenen Prüffälle wie für eigene Übungen | 90 Tests erfolgreich |
| Notizprogramm | CRUD, Validierung, leere Daten, IDs, JSON-Rundlauf und simuliertes Speicherproblem | 12 Tests erfolgreich |
| Projektvorlage | Lokal als editierbares Paket ohne zusätzliche Laufzeitabhängigkeiten installiert | Installation erfolgreich |
| Projektvorlage | Anwendung mit `python -m starter_app Basti` gestartet | `Hallo Basti!` |
| Projektvorlage | Tests für Fachfunktion und Kommandozeile | 6 Tests erfolgreich |
| Projektvorlage | Ruff 0.16.9: ausgewählte Lint-Regeln | Bestanden |
| Projektvorlage | Ruff 0.16.9: Formatprüfung nach Formatierung | Bestanden |
| Projektvorlage | mypy 2.3.1: strikte Prüfung von vier Quelldateien unter src | Bestanden |
| Python-Dateien | Alle enthaltenen Python-Dateien syntaktisch geparst, einschließlich Starterdateien | Bestanden |
| Projektkonfiguration | pyproject.toml mit tomllib gelesen | Bestanden |
| Navigation | Lokale Markdown-Verweise auf vorhandene Dateien geprüft | Bestanden |
| Terminalsuche | Mehrwortsuche nach Datei/lesen | Passende Kapitel und Übung gefunden |
| Offline-Ansicht | JavaScript in einer DOM-Testumgebung ausgeführt: Startseite, Suche, Navigation, Inhaltsverzeichnis, Lösungenfilter, leere Suche und interne Dokumentlinks | Bestanden |

## Was diese Ergebnisse bedeuten

Insgesamt wurden 108 äußere unittest-Prüffälle ausgeführt, zusätzlich die 90 ausführbaren Kapitelbeispiele. Die Übung zum Schreiben eigener Tests enthält darüber hinaus ihre eigenen drei Tests innerhalb einer Prüfung. Die ungefüllten Starterdateien sollen zu Beginn fehlschlagen; ihr Fehlerzustand ist beabsichtigt.

Die dokumentierten Beispielausgaben wurden aus tatsächlichen Programmläufen erzeugt und später erneut verglichen. Das ist eine Konsistenzprüfung zwischen Code und Dokumentation. Die zusätzlichen Aufgabe- und Projekttests prüfen unabhängig formulierte Anforderungen wie Randwerte, Fehlerfälle und unveränderte Eingaben.

## Nicht ausgeführte Prüfungen und Grenzen

- Kein echter Windows-/PowerShell-Testlauf; die zugehörigen Befehle wurden für diese Umgebung formuliert.
- Kein vollständiger visueller Browser-Test. Die Browserdatei ließ sich in der Arbeitsumgebung nicht erfolgreich herunterladen. Die Offline-Ansicht wurde stattdessen strukturell und funktional in einer DOM-Testumgebung geprüft; das ersetzt keine Prüfung des tatsächlichen Layouts auf jedem Bildschirm.
- Keine Live-HTTP-Anfragen an externe APIs; das Netzwerkbeispiel verwendet eine simulierte Antwort.
- Kein vollständiger Test aller neueren Python-Versionen, Paketversionen und denkbaren Eingaben.
- Ruff und mypy wurden auf die professionelle Projektvorlage angewendet. Lernbeispiele zeigen teilweise bewusst einfache oder problematische Muster zur Erklärung und unterliegen nicht pauschal denselben Regeln.
- Die lokale Installationsprüfung verwendete eine getrennte virtuelle Umgebung mit bereits verfügbaren Build-Werkzeugen. Ein vollständiger Release-Build und eine Veröffentlichung waren nicht Teil dieses Auftrags.

Die Versionsangaben der geprüften Entwicklungswerkzeuge sind ein Prüfstand. Die Vorlage installiert über `[dev]` derzeit ungesperrte Werkzeugversionen. Für dein konkretes Projekt solltest du nach eigenen erfolgreichen Prüfungen einen kontrollierten Abhängigkeitsstand festhalten; siehe Projektleitfaden.
