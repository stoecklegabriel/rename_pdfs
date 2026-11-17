NHM PDF Renamer
Python-Skript zur automatischen Ermittlung NHM-konformer Dateinamen aus wissenschaftlichen PDF-Dateien.

Ziel
Aus PDFs sollen automatisch

Autor*innen
Publikationsjahr
Titel
extrahiert werden, um Dateinamen nach dem NHM-Schema zu erzeugen.

Beispiel:

Shen_Z_et_al_2024_Three_New_Species_of_deep-sea.pdf
Technischer Ablauf
PDF mit PyMuPDF auslesen
Text auf maximal 15.000 Zeichen begrenzen
Anfrage an ein lokales LLM
Extraktion von Autor*innen, Jahr und Titel
Erzeugung eines NHM-konformen Dateinamens
Ausgabe als CSV
Ergebnisse
Verarbeitete PDFs: 3.290

2.385 automatisch zugeordnet
905 manuell nachzubearbeiten
Automatische Erkennungsquote: 72,5 %

Verwendete Bibliotheken
PyMuPDF
requests
pandas
Hinweis
Das Projekt entstand als Prototyp zur Unterstützung der Bearbeitung wissenschaftlicher PDF-Bestände am NHM Wien.
