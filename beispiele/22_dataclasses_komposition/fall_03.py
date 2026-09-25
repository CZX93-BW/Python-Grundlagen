"""Dataclasses, Komposition und Vererbung: Eine Klasse gezielt erweitern."""

class Report:
    def describe(self):
        return "Bericht"

class WeeklyReport(Report):
    def describe(self):
        return super().describe() + " für eine Woche"

print(WeeklyReport().describe())
