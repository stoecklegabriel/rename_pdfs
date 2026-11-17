# NHM PDF Renamer

Automatische Ermittlung NHM-konformer Dateinamen aus wissenschaftlichen PDF-Dateien mithilfe von Python, PyMuPDF und einem lokalen Large Language Model (LLM).

## Überblick

Dieses Projekt wurde entwickelt, um große Bestände wissenschaftlicher PDF-Dateien effizient nach einem einheitlichen Schema zu benennen.

Da Autorinnen und Autoren, Publikationsjahr und Titel häufig nicht zuverlässig in den PDF-Metadaten hinterlegt sind und wissenschaftliche Publikationen sehr unterschiedliche Layouts aufweisen, nutzt das Skript ein Large Language Model zur Extraktion der benötigten bibliographischen Informationen.

## Namensschema

Dateien werden nach folgendem Muster benannt:

```text
Nachname_Initialen_Jahr_Erste_Fünf_Titelwörter.pdf
```

### Beispiele

```text
Mah_CL_2006_A_new_species_of_Xyloplax.pdf

Lawrence_JM_&_Pomory_CM_1999_Anterior-posterior_asymmetry_in_the_Aristotles_lantern.pdf

Shen_Z_et_al_2024_Three_New_Species_of_deep-sea.pdf
```

### Regeln

#### Eine Autorin / ein Autor

```text
Nachname_Initialen_Jahr_Titel.pdf
```

#### Zwei Autorinnen / Autoren

```text
Nachname1_Initialen_&_Nachname2_Initialen_Jahr_Titel.pdf
```

#### Drei oder mehr Autorinnen / Autoren

```text
Nachname1_Initialen_et_al_Jahr_Titel.pdf
```

Weitere Regeln:

- Es werden nur die ersten fünf Titelwörter verwendet.
- Leerzeichen werden durch Unterstriche ersetzt.
- Diakritische Zeichen werden normalisiert.
- Die Umlaute ä, ö und ü bleiben erhalten.

---

## Workflow

```text
3.290 PDF-Dateien
        │
        ▼
Pakete à ca. 200 PDFs
        │
        ▼
Textextraktion mit PyMuPDF
        │
        ▼
Begrenzung auf 15.000 Zeichen
        │
        ▼
Lokales LLM
        │
        ▼
Extraktion von Autorinnen und Autoren,
Publikationsjahr und Titel
        │
        ▼
Erzeugung eines NHM-konformen
Dateinamenvorschlags
        │
        ▼
CSV-Ausgabe
        │
        ▼
Gesamtauswertung
       / \
      /   \
     ▼     ▼

2.385 automatisch            905 manuell
zugeordnet                   nachzubearbeiten
```

---

## Technischer Ansatz

1. Einlesen der PDF-Dateien mit PyMuPDF
2. Extraktion des Volltextes
3. Begrenzung auf maximal 15.000 Zeichen

```python
text = text[:15000]
```

4. Übermittlung des Textes an ein lokales LLM
5. Extraktion von:
   - Autorinnen und Autoren
   - Initialen
   - Publikationsjahr
   - Titel
6. Erzeugung eines NHM-konformen Dateinamens
7. Speicherung der Ergebnisse in einer CSV-Datei

---

## Ergebnisse

| Kennzahl | Wert |
|-----------|------:|
| Verarbeitete PDF-Dateien | 3.290 |
| Automatisch zugeordnet | 2.385 |
| Manuell nachzubearbeiten | 905 |
| Automatische Erkennungsquote | 72,5 % |

Die Verarbeitung erfolgte in Paketen von jeweils etwa 200 PDF-Dateien mit einer durchschnittlichen Laufzeit von rund 20 Minuten pro Paket.

---

## Verwendete Technologien

- Python
- PyMuPDF
- Requests
- Pandas
- Lokales Large Language Model (LLM)

---

## Projektstatus

Proof of Concept / Forschungs- und Automatisierungsprojekt

Das Projekt zeigt, dass sich ein großer Bestand wissenschaftlicher PDF-Dateien mit vertretbarem Aufwand automatisiert analysieren und nach einer einheitlichen Konvention benennen lässt. Durch die automatische Verarbeitung konnten mehr als zwei Drittel der Dateien ohne manuelle Recherche zugeordnet werden.

---

## Mögliche Weiterentwicklungen

- Analyse ausschließlich der ersten ein bis zwei Seiten
- Offizielle API-Anbindung statt Session-Token
- Verbesserte Behandlung von OCR- und Scan-Dokumenten
- Automatische Umbenennung nach manueller Freigabe
- Integration in bestehende NHM-Workflows
