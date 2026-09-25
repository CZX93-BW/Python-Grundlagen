# Eigene Themen ergänzen

[Start](../README.md) · [Index](../INDEX.md)

Diese Sammlung soll mit dir wachsen. Ergänze lieber einen gut erklärten Fall, den du wirklich verstanden hast, als viele unkommentierte Codekopien.

## Ablauf

1. Vergib eine klare Nummer und einen sprechenden Namen, beispielsweise `31_http_fehler.md`.
2. Erstelle das Kapitel unter `kapitel` und passende `.py`-Dateien unter `beispiele`.
3. Übernimm die Struktur der nachfolgenden Vorlage. Erkläre neue Fachbegriffe direkt.
4. Führe jeden Codefall aus und übernimm seine tatsächliche Ausgabe.
5. Ergänze Übung und Lösung getrennt, mit eindeutigen Anforderungen und denselben Nummern.
6. Ergänze den Index und den passenden Lernpfad.
7. Erzeuge die Offline-Ansicht neu: `python ./werkzeuge/handbuch_bauen.py`.

Die vorhandene Übungsprüfung ist auf Nummern 1–30 eingestellt. Für zusätzliche automatisierte Übungen musst du ihren erlaubten Zahlenbereich in `werkzeuge/uebung_pruefen.py` erweitern und eine passende Testdatei im vorhandenen Format ergänzen. Die Beispielprüfung verwendet `95_tests/beispiele.json`; neue Fälle werden dort mit relativen Pfaden, vorbereiteten Eingaben und überprüfter Standardausgabe eingetragen. Die globale Suche und die Offline-Ansicht finden neue Markdown-Dateien automatisch.

## Kapitelvorlage

```markdown
# Nummer · Thema

## Wozu brauche ich das?
Ein konkretes Alltagsproblem und wann diese Technik passt.

## Erst verstehen
Neue Begriffe und notwendiges Vorwissen erklären.

## Fall 1: Eine konkrete Frage
Ziel, vollständiger Code, echte Ausgabe und Erklärung der Schritte.

## Weitere wichtige Fälle
Leere Eingaben, fehlende Werte und typische Grenzen bearbeiten.

## Typische Stolperstellen
Erklären, welcher Fehler warum entsteht und wie man ihn vermeidet.

## Selbst anwenden
Auf die Übung verlinken; die Lösung bleibt im getrennten Ordner.

## Quellen
Offizielle Dokumentation mit passender Version verlinken.
```

## Qualitätsfragen

- Ist der Code vollständig ausführbar oder deutlich als Ausschnitt bezeichnet?
- Sind Voraussetzungen, benötigte Pakete und Dateipfade erklärt?
- Weiß ich, ob eine Eingabe verändert wird?
- Sind Fehlerfälle dokumentiert und passende Beispiele geprüft?
- Kann eine lernende Person jeden neuen Begriff im Text oder Glossar finden?
- Sind mögliche Netzwerkzugriffe und Dateiveränderungen ersichtlich?

Django und andere Frameworks sollten später einen eigenen Themenbereich erhalten. So vermischst du Sprachgrundlagen nicht mit Regeln eines bestimmten Frameworks.
