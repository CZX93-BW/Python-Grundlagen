# Leitfaden: ein verständliches, professionell aufgebautes Python-Projekt

[Start](../README.md) · [Kopierbare Projektvorlage](../85_projektvorlage/README.md) · [Checkliste](PROJEKT_CHECKLISTE.md)

Dieser Leitfaden begleitet dich vom neuen Ordner bis zu einem geprüften Projektstand. Professionell bedeutet hier: Andere können das Projekt einrichten, sein Verhalten verstehen, Änderungen prüfen und Fehler nachvollziehen. Dafür brauchst du nicht möglichst viele Werkzeuge und Ordner.

Die Vorlage ist ein kleines Terminalprogramm. Für Django, eine Web-API, Datenanalyse oder ein verteiltes System kommen zusätzliche Fachkonventionen hinzu. Es gibt keine einzige Struktur und keine Checkliste, die für jedes Python-Projekt automatisch vollständig richtig ist.

## Schritt 1: Den Auftrag in drei Sätzen festhalten

Schreibe vor dem ersten Code in die README:

1. **Zweck:** Welches konkrete Problem löst das Programm?
2. **Ein- und Ausgabe:** Welche Daten kommen hinein, welches Ergebnis entsteht?
3. **Fertig bedeutet:** Woran erkennst du, dass die Funktion funktioniert?

Beispiel für ein Notizprogramm: „Ich verwalte lokale Notizen. Titel und Text werden im Terminal eingegeben und in JSON gespeichert. Nach einem Neustart sind gespeicherte Notizen wieder verfügbar; leere Titel werden mit einer Meldung abgelehnt.“

Ergänze ausdrücklich, was vorerst außerhalb des Umfangs liegt, etwa mehrere Benutzer oder Cloud-Synchronisierung. So verhinderst du, dass dein Lernprojekt unbemerkt immer größer wird.

## Schritt 2: Eine passende Struktur wählen

Für ein einmaliges Skript können `main.py`, `README.md` und ein kleiner Testordner ausreichen. Für eine wachsende Anwendung oder ein installierbares Paket verwendest du die mitgelieferte Vorlage:

| Pfad | Verantwortung |
| --- | --- |
| `pyproject.toml` | Projektbeschreibung, Python-Version, Abhängigkeiten und Werkzeugregeln |
| `README.md` | Einrichtung, Start, Tests und bekannte Grenzen |
| `src/starter_app/` | Importierbarer Anwendungscode |
| `src/starter_app/service.py` | Fachliche Berechnung/Validierung ohne Ein- und Ausgabe |
| `src/starter_app/cli.py` | Kommandozeile, Anzeige und Fehlercodes |
| `src/starter_app/__main__.py` | Start mit `python -m starter_app` |
| `tests/` | Automatische Verhaltenstests |
| `.gitignore` | Generierte Dateien, lokale Umgebung und Geheimnisse ausschließen |
| `.env.example` | Dokumentierte Beispielwerte ohne echte Geheimnisse |

Warum `src`? Dein Paket liegt dadurch getrennt von den sonstigen Projektdateien. Du installierst es zum Entwickeln ausdrücklich in deine Umgebung. Das verringert versehentliche erfolgreiche Imports nur deshalb, weil du gerade im Projektordner stehst. Für kleine Lernskripte ist diese Trennung optional.

Erstelle nicht vorsorglich Ordner wie `managers`, `factories`, `helpers` und `utils`, wenn es noch keinen konkreten Inhalt gibt. Ein Dateiname wie `invoice_calculation.py` erklärt seine Aufgabe besser als `helpers.py`.

## Schritt 3: Die Vorlage kopieren und die Umgebung anlegen

Kopiere `85_projektvorlage` an einen neuen Ort und öffne **diesen neuen Projektordner** in VS Code. Ändere zunächst nur Name und Beschreibung in `pyproject.toml`. Der Importname `starter_app` darf zum ersten Ausprobieren bestehen bleiben.

Im PowerShell-Terminal des neuen Projekts:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m starter_app "Basti"
```

Wenn nur `python` verfügbar ist, ersetze den ersten `py`-Teil entsprechend. Python muss mindestens Version 3.12 haben. Die Ausgabe des Programms lautet `Hallo Basti!`.

Die direkte Angabe des `.venv`-Interpreters funktioniert ohne Aktivierung. Wenn du aktivieren möchtest, verwende `.\.venv\Scripts\Activate.ps1`. Wird das blockiert, bleibe bei den expliziten Pfaden; eine Änderung der Ausführungsrichtlinie ist für diese Anleitung nicht erforderlich.

Wähle in VS Code denselben Interpreter. `python -m pip` koppelt Paketinstallation an den angegebenen Python-Interpreter. `-e` bedeutet **editable**: Dein lokaler Quellcode bleibt direkt für die installierte Entwicklungsversion verwendbar. `[dev]` installiert zusätzlich die unter diesem Namen aufgeführten Entwicklungswerkzeuge.

## Schritt 4: pyproject.toml verstehen

Öffne die Datei in der Vorlage. Ihre wichtigsten Bereiche:

| Abschnitt | Bedeutung |
| --- | --- |
| `[build-system]` | Welches Werkzeug dein Paket baut und welche Build-Abhängigkeiten es braucht |
| `[project]` | Name, Version, Beschreibung, Python-Mindestversion und Laufzeitabhängigkeiten |
| `[project.optional-dependencies]` | Hier die extra installierbaren Entwicklungswerkzeuge |
| `[project.scripts]` | Ein Terminalbefehl und die dazugehörige Python-Einstiegsfunktion |
| `[tool.setuptools.packages.find]` | Wo die importierbaren Pakete liegen |
| `[tool.ruff]` | Gemeinsame Regeln für Codeprüfung und Formatierung |
| `[tool.mypy]` | Einstellungen für statische Typprüfung |

Der Distributionsname `python-project-starter` und der Importname `starter_app` müssen nicht identisch sein. Bindestriche sind für den Importnamen ungeeignet. Wenn du den Paketordner umbenennst, passe Imports und Einstiegspunkt ebenfalls an und installiere das Projekt erneut mit `-e`.

Die Vorlage veröffentlicht nichts und wählt keine Lizenz in deinem Namen. Eine spätere Veröffentlichung braucht eigene Entscheidungen zu Namen, Metadaten, Lizenz und Zugangsdaten.

## Schritt 5: Abhängigkeiten bewusst verwalten

Die Vorlage hat keine zusätzlichen Laufzeitpakete. `ruff`, `mypy` und `build` sind Entwicklungswerkzeuge. Nimm nur Pakete auf, die einen konkreten Nutzen haben. Prüfe zuerst, ob die Standardbibliothek die Aufgabe verständlich abdeckt.

**Laufzeitabhängigkeiten** werden zum Ausführen benötigt. **Entwicklungsabhängigkeiten** dienen etwa Tests, Prüfungen oder Paketbau. Halte diese Bedeutungen getrennt. In einem größeren Team kann dafür auch ein Werkzeug mit Dependency Groups und Lockdatei verwendet werden; die Vorlage hält den Start mit pip bewusst einfach.

Die Vorlage legt die Entwicklungswerkzeuge noch nicht auf exakte Versionen fest. Das erleichtert den Einstieg, ist aber kein reproduzierbar gesperrter Release-Stand. Gehe für dein echtes Projekt so vor:

1. Installiere in einer frischen Umgebung und führe alle Prüfungen aus.
2. Dokumentiere die tatsächlich eingesetzte Python-Version.
3. Halte die erfolgreich geprüften Paketversionen mit einem konsistent verwendeten Lock-/Requirements-Verfahren fest.
4. Prüfe nach Updates erneut. Ein gesperrter Stand soll aktualisiert werden können, aber kontrolliert.

Ein einfacher pip-basierter Lernschritt nach einer geprüften Installation ist:

```powershell
.\.venv\Scripts\python.exe -m pip freeze --exclude-editable | Set-Content -Encoding utf8 requirements-dev.txt
```

Das ist eine Momentaufnahme installierter Pakete, keine plattformübergreifende Garantie und keine automatische Sammlung aller isolierten Build-Abhängigkeiten. Prüfe den Inhalt auf lokale Pfade und unerwünschte Pakete. Die Datei ersetzt auch nicht die direkten Projektabhängigkeiten in `pyproject.toml`.

Zum Nachvollziehen in einer frischen Umgebung installierst du zuerst diese geprüfte Datei und anschließend das eigene Paket:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pip install -e .
```

Wenn ein Projekt auf verschiedenen Betriebssystemen ausgerollt wird oder exakte Builds braucht, verwende ein dafür geeignetes Lock-Verfahren mit klarer Aktualisierungsstrategie. Vermische nicht mehrere konkurrierende Paketmanager ohne Grund.

## Schritt 6: Mit einer kleinen Fachfunktion beginnen

Lies `service.py` der Vorlage. Die Funktion nimmt einen Namen entgegen und liefert einen Text. Sie liest nicht selbst von der Tastatur und schreibt keine Datei. Dadurch kannst du sie aus einer CLI, einem späteren Web-Endpunkt oder einem Test aufrufen.

Für eine neue Funktion beantworte zunächst:

- Welche Parameter braucht sie wirklich?
- Was gibt sie bei Erfolg zurück?
- Welche Eingaben sind ungültig?
- Verändert sie übergebene Daten? Falls ja, ist das ausdrücklich gewollt?

Vermeide globale veränderbare Listen als versteckten Zustand. Übergib benötigte Daten oder fasse zusammengehörigen Zustand in einer passenden Klasse zusammen. Baue noch kein Repository- oder Service-Framework, wenn zwei verständliche Funktionen ausreichen.

## Schritt 7: Clean Code konkret anwenden

| Regel | Verständliche Anwendung |
| --- | --- |
| Sprechende Namen | `price_in_cents` statt `p`; Einheit im Namen, wenn sie leicht verwechselt werden kann |
| Python-Konventionen | `snake_case` für Funktionen/Variablen, `PascalCase` für Klassen, `UPPER_CASE` für Konstanten |
| Kleine Verantwortung | Eine Funktion prüft/berechnet; eine andere steuert die Ausgabe |
| Klare Rückgaben | Nicht je nach Fehler zufällig mal Zahl, mal Fehlermeldung als Text liefern |
| Frühe Sonderfallprüfung | Ungültige Eingaben zuerst zurückweisen, danach den normalen Ablauf lesen |
| Wenig Verschachtelung | Kleine Hilfsfunktionen oder frühe Rückgaben verwenden, wenn sie den Ablauf vereinfachen |
| Dopplung mit Bedacht beseitigen | Gemeinsame stabile Logik auslagern, nicht zufällig ähnliche Zeilen zwanghaft vereinigen |
| Einfachste passende Lösung | Keine Klasse, Vererbung oder Async-Struktur ohne konkreten Nutzen |
| Gründe dokumentieren | Warum eine Regel existiert; offensichtlichen Code nicht Zeile für Zeile wiederholen |
| Seiteneffekte sichtbar machen | Benennen und dokumentieren, wenn Dateien geschrieben oder Daten verändert werden |

Eine starre Vorgabe wie „jede Funktion höchstens 14 Zeilen“ ist keine allgemeine Python-Best-Practice. Nutze eine kleine, verständliche Verantwortung als Kriterium. Eine künstlich zerlegte Funktion kann schwerer verständlich werden. PEP 8 beschreibt Konventionen; im Team gelten vereinbarte Regeln konsistent. Die Vorlage nutzt Ruff-Formatierung mit 88 Zeichen als bewusste Projekteinstellung, keine Behauptung über das einzige gültige Zeilenlimit.

**DRY** heißt, Wissen nicht widersprüchlich mehrfach zu pflegen. **KISS** heißt, unnötige Komplexität zu vermeiden. **YAGNI** erinnert daran, nicht vorsorglich Funktionen für nur vermutete Anforderungen zu bauen. SOLID-Prinzipien können bei größerer objektorientierter Software helfen, verlangen aber nicht für jedes kleine Skript Interfaces und Vererbung.

## Schritt 8: Typen und Dokumentation ergänzen

Annotiere zuerst die öffentlich verwendeten Funktionen. Beispiel: `name: str` und `-> str`. Ist `None` eine erlaubte Antwort, drücke das im Rückgabetyp aus. `Any` löst einen unklaren Vertrag nicht, sondern schaltet an dieser Stelle einen Teil der Typprüfung aus.

Eine hilfreiche Docstring erklärt in einem Satz den Zweck. Ergänze bei Bedarf Parameterbedeutung, Rückgabewert, Ausnahmen und wichtige Seiteneffekte. Type Hints ersetzen keine Prüfung fremder JSON-Daten oder Terminaleingaben. Verlinke ungewöhnliche fachliche Entscheidungen in einer kurzen Projektnotiz.

Die README sollte mindestens enthalten: Zweck, unterstützte Python-Version, Einrichtung, Startbefehl, Prüfkommandos, Konfiguration und bekannte Grenzen. Eine andere Person soll den ersten erfolgreichen Start ohne Vermutungen durchführen können.

## Schritt 9: Fehler an sinnvollen Stellen behandeln

Prüfe Eingaben an den Grenzen des Systems: Terminal, Datei, Netzwerk oder Datenbank. Fange gezielt Fehler ab, auf die du sinnvoll reagieren kannst. Ein Dienst kann `ValueError` auslösen; die CLI zeigt daraus eine verständliche Meldung und liefert einen Fehlercode.

Nutze `with` für Ressourcen. Vermeide `except Exception: pass`. Verwende `raise ... from error`, wenn ein technischer Fehler in einen fachlichen Fehler übersetzt wird. Logge unerwartete Fehler mit Kontext, aber ohne Zugangsdaten oder vollständige sensible Nutzdaten.

Verwende `pathlib` und eine ausdrücklich gewählte Textkodierung. Nutze Platzhalter für SQL-Werte. Führe fremde Texte nicht mit `eval()` aus und lade keine nicht vertrauenswürdigen Pickle-Dateien. Verwende für Sicherheits-Tokens `secrets`. Das sind konkrete Regeln für diese Schnittstellen, kein Ersatz für ein Sicherheitskonzept einer späteren Web-Anwendung.

## Schritt 10: Aussagekräftige Tests schreiben

Die Vorlage verwendet `unittest` aus der Standardbibliothek. Für größere Projekte kann pytest eine sinnvolle Alternative sein; du musst nicht beide gleichzeitig einsetzen.

Für eine Funktion mit mehreren wichtigen Fällen:

1. Prüfe einen typischen gültigen Wert.
2. Prüfe fachlich wichtige Grenzen, beispielsweise null oder eine leere Liste.
3. Prüfe den erwarteten Fehlerfall.
4. Prüfe unerwünschte Änderungen an Eingaben, falls Unverändertheit zum Vertrag gehört.

Teste Verhalten statt interner Umsetzung. Eine Umbenennung einer lokalen Variablen soll keinen fachlichen Test brechen. Verwende temporäre Ordner für Dateitests und ersetze echte Netzwerkgrenzen durch gezielte Testobjekte. Setze Mocks sparsam ein, damit nicht nur deine eigene Testattrappe geprüft wird.

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Nach einem gefundenen Fehler: Erzeuge einen kleinen Test, der genau dieses Problem sichtbar macht. Behebe die Ursache und prüfe danach den betroffenen Bereich. Hohe Testabdeckung allein beweist keine fachliche Korrektheit.

## Schritt 11: Automatische Qualitätsprüfungen nutzen

Führe im Projektordner aus:

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m mypy
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

- **Ruff check** findet ausgewählte problematische Muster, ungenutzte Imports und weitere Regelverstöße.
- **Ruff format** sorgt für einheitliche Formatierung. Ohne `--check` verändert es Dateien.
- **mypy** vergleicht Typverträge mit ihrer Verwendung. Die Vorlage prüft den Anwendungscode unter `src` streng.
- **unittest** führt die angegebenen Verhaltensprüfungen aus.

Lies jede Meldung. Setze kein pauschales `ignore`, nur um Grün zu bekommen. Wenn eine Ausnahme begründet ist, begrenze sie auf die betroffene Stelle und halte den Grund fest. Ein Formatter entscheidet über Darstellung, nicht über Architektur oder Fachlogik.

Die Dateien dieser Vorlage wurden hier syntaktisch und funktional geprüft. Ruff und mypy wurden ebenfalls erfolgreich auf die Vorlage angewendet. Die genauen Versionen und Grenzen stehen im Prüfbericht.

## Schritt 12: Versionierung und automatische Prüfung vorbereiten

Halte Änderungen klein und thematisch zusammengehörig. Prüfe vor einem Commit den Diff. Nimm Code, Tests, Konfiguration und relevante Dokumentation gemeinsam auf. Virtuelle Umgebungen, Zugangsdaten, Caches und generierte Build-Dateien gehören üblicherweise nicht ins Repository. Eine `.gitignore` entfernt keine bereits versionierten Geheimnisse aus der Historie.

Mögliche Commit-Nachrichten beschreiben eine konkrete Änderung, etwa `feat(notes): validate titles before saving` oder `test(notes): cover missing note IDs`. Ein bestimmtes Präfixschema ist eine Projektkonvention, keine Python-Pflicht.

Wenn du GitHub Actions oder eine andere CI einrichtest, übertrage zunächst genau die lokal funktionierenden Schritte:

1. Repository auschecken und die unterstützte Python-Version einrichten.
2. Abhängigkeiten aus dem vereinbarten geprüften Stand installieren.
3. Projekt installieren.
4. Linter, Formatprüfung, Typprüfung und Tests starten.
5. Den Lauf bei einem Fehler fehlschlagen lassen.

Starte mit einer Version. Versprich mehrere unterstützte Python-Versionen erst, wenn du sie auch prüfst. Einen plattformspezifischen Fehler erkennst du nur durch einen entsprechenden Lauf oder eine gezielte plattformunabhängige Gestaltung. Eine CI-Veröffentlichung, ein Deployment oder ein Push wird durch diese Vorlage nicht eingerichtet oder ausgelöst.

## Schritt 13: Einen fertigen Stand prüfen

Nutze die [separate Checkliste](PROJEKT_CHECKLISTE.md). Führe die Einrichtung zumindest einmal in einer frischen Umgebung aus. Dadurch findest du Abhängigkeiten, die bisher nur zufällig global installiert waren.

Wenn das Projekt als Paket verteilt werden soll:

```powershell
.\.venv\Scripts\python.exe -m build
```

Installiere das erzeugte Wheel anschließend in einer frischen Umgebung und prüfe den Start. Editable-Installation und installiertes Paket können unterschiedliche Verpackungsprobleme sichtbar machen. Veröffentliche erst nach eigener Prüfung von Paketinhalt, Metadaten und Lizenz. Für eine lokal verwendete kleine Anwendung ist eine PyPI-Veröffentlichung nicht erforderlich.

## Später ergänzen, wenn es gebraucht wird

| Konkreter Bedarf | Passende Erweiterung |
| --- | --- |
| Mehrere zusammengehörige Fachbereiche | Fachlich geschnittene Module oder Unterpakete |
| Viele Datensätze oder konkurrierende Zugriffe | Datenbank, Transaktionen und Migrationsstrategie |
| Web-API | Framework-Konventionen, Schema-Validierung, Authentifizierung und API-Tests |
| Wiederkehrende Datenänderungen | Migrationen und getestete Wiederherstellung |
| Produktionsbetrieb | Betriebslogs, Überwachung, Backups, Update- und Rollback-Ablauf |
| Viele externe Abhängigkeiten | Lock-Verfahren, überprüfte Updates und passende Abhängigkeitsanalyse |
| Gemessene Engpässe | Profiling und gezielte Optimierung |

Baue diese Themen bei tatsächlichem Bedarf aus. Ein kleines Projekt, das jemand versteht, reproduzierbar startet und sicher ändern kann, ist eine bessere Grundlage als eine große ungeprüfte Architektur.
