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
Extraktion von Autor*innen,
Publikationsjahr und Titel
*       │
        ▼
Erzeugung*eines NH*-konformen
Dateinamenv*rschlags
        │
        ▼
CSV*Ausgabe
        │
        ▼
Ges*mtauswertung
       / \
      /*  \
     ▼    *▼

2.385 automatisch     *905 manuell
zugeordnet            *nachzubearbeiten
```

---

## Tech**scher Ansatz

1* Einlesen der PDF-Dateien*mit PyMuPDF
2. Extraktion des*Volltext*s
3. Begrenzung auf maximal *5.000 Zeichen

```python
text =*text[:15000]
```

4. Über*ittlung des Textes an ein lokales *LM*5. Extraktion von:
   - Autor*nnen und Autoren
   - Initial*n
   - Publikationsjahr
   -*Titel
6. Erzeugung eines NHM*konformen Dateinamens
7. Speicheru*g der*Ergebnisse in einer CSV-Datei

---*
## Ergebnisse*
| Kennzahl | Wert |
|-----------*------:|
| Verarbeitete PDF-Date*en | 3.290 |
| Automatisch*zugeordnet | 2.385 |
| Man*ell nachzubearbeiten | 905 |
|*Automatische Erkennungsquote | 72,* % |

Die Verarbeitung erfolgte in*Pak*ten von jeweils etwa 200 PDF*Dateien mit einer durchschnittlich*n Laufzeit*von rund 20 Minuten pro Paket.

--*

## Verwendete Technologien

- Py*hon
- PyMuPDF*- Requests
- Pandas
- Lok*les Large Language Model (LLM)

--*

##*Projektstatus

Proof of*Concept / Forschungs-*und Automatisierungsprojekt

*as Projekt zeigt, dass sich*ein großer Bestand*wissenschaftlicher PDF-Dateien mit*vert*etbarem Aufwand automatisiert anal*s*eren und nach einer einheitlichen *onvention benennen lässt.*Durch die automatische*Verarbeitung konnten mehr als zwei*Dritt*l der Dateien ohne manuelle Recher*he*zugeordnet werden.

---

##*Mögliche Weiterentwicklungen*
- Analyse ausschließlich der erst*n ein*bis zwei Seiten
- Off*zielle API-An*indung statt Session-Token
- Verbe*ser*e Behandlung von OCR* und Scan-Dokumenten
* Automatische Um*enennung nach manueller Freigabe
-*Integration in bestehende NHM-*orkflows
