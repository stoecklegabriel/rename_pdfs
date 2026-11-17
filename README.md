# NHM PDF Renamer

Python-Skript zur automatischen Ermittlung NHM-konformer Dateinamen aus wissenschaftlichen PDF-Dateien mithilfe von PyMuPDF und einem lokalen Large Language Model (LLM).

## Hintergrund

Für einen Bestand von **3.290 wissenschaftlichen PDF-Dateien** sollten Autor*innen, Publikationsjahr und Titel automatisch erkannt werden, um Dateinamen nach einem einheitlichen NHM-Schema zu erzeugen.

Beispiel:

```text
Mah_CL_2006_A_new_species_of_Xyloplax.pdf

Lawrence_JM_&_Pomory_CM_1999_Anterior-posterior_asymmetry_in_the_Aristotles_lantern.pdf

Shen_Z_et_al_2024_Three_New_Species_of_deep-sea.pdf
```

Die benötigten Informationen liegen in wissenschaftlichen Publikationen häufig nicht als strukturierte Metadaten vor. Insbesondere ältere Arbeiten weisen sehr unterschiedliche Layouts und Formatierungen auf, wodurch regelbasierte Verfahren oft an ihre Grenzen stoßen.

## Ziel

Automatische Ermittlung von:

- Autor*innen
- Publikationsjahr
- Titel

und Erzeugung NHM-konformer Dateinamenvorschläge.

## Technischer Ablauf

```text
3.290 PDF-Dateien
        │
        ▼
Pakete à ca. 200 PDFs
        │
        ▼
PyMuPDF Textextraktion
        │
        ▼
max. 15.000 Zeichen
        │
        ▼
Lokales LLM
(gpt.nhm.at:8080)
        │
        ▼
Extraktion von
Autor*innen* Jahr und Titel
        │
        **NHM-Dateinam*nvorschlag
        │
       *▼
CSV-Ausgabe
        │
       *▼
Gesamtauswertung
      */ \
      /   \
    *▼     ▼

-        2.385 automatisch* zugeordnet
-        905 manuell nachzubearbeiten

##*Vorgehensweise

1. PDF-Dateien mit **PyMuPDF** einlesen.
2. Text aus den Dokumenten extrahieren.
3. Extrahierten Text auf maximal 15.000 Zeichen begrenzen:

```python
text =*text[:15000]
```

4. Übermittlung des Textes an ein lokales LM
5. Extraktion von:
   - Nach*amen
   - Initialen
   - Publikationsjahr
   - Titel
6. Erzeugung eines NHM-konformen Dateinamens
7. Speicherung der Ergebnisse in einer CSV-Date.

## Namenskon*ention

### Eine Autorin /*ein Autor

```text
Nach*ame_Initialen_Jahr_Titelwort_Titelwort2_Titel*ort3_Titelwort4_Titelwort5.pdf
```

Beispiel:

```text*Mah_CL_2006_A_new_species_of*Xyloplax.pdf
```

### Zwei*Autor*innen

```text
Nachname1_Initialen_&_Nachname2_Initialen_Jahr_Titel.pdf
``*

Beispiel:

```text
Lawrence_JM_&_Pomory_CM_1999_Anterior-posterior_asymmetry_in_th**
