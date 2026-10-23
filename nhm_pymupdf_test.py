import fitz
import pandas as pd
import re
from pathlib import Path

# ==========================================================
# KONFIGURATION
# ==========================================================

PDF_FOLDER = Path(
    r"C:\PDFS\0005_20080607_bis_20081206"
)

OUTPUT_CSV = "0005_Analyse.csv"

MAX_FILES = 200

# ==========================================================
# TEXT AUS ERSTEN 3 SEITEN
# ==========================================================

def extract_text(pdf_file):

    text = ""

    try:

        doc = fitz.open(pdf_file)

        for page in doc[:3]:

            text += page.get_text()

        doc.close()

    except Exception as e:

        print(
            f"Fehler bei {pdf_file.name}: {e}"
        )

    return text


# ==========================================================
# TITEL ÜBER SCHRIFTGRÖSSE FINDEN
# ==========================================================

def extract_title(pdf_file):

    try:

        doc = fitz.open(pdf_file)

        page = doc[0]

        data = page.get_text("dict")

        candidates = []

        for block in data["blocks"]:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                line_text = ""
                max_size = 0

                for span in line["spans"]:

                    line_text += span["text"]

                    max_size = max(
                        max_size,
                        span["size"]
                    )

                line_text = line_text.strip()

                if len(line_text) > 10:

                    candidates.append(
                        (
                            max_size,
                            line_text
                        )
                    )

        doc.close()

        if not candidates:
            return ""

        candidates.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return candidates[0][1]

    except:

        return ""


# ==========================================================
# JAHR ERKENNEN
# ==========================================================

def extract_year(text):

    years = re.findall(
        r"(18\d{2}|19\d{2}|20\d{2})",
        text
    )

    if years:

        return years[0]

    return ""


# ==========================================================
# HAUPTPROGRAMM
# ==========================================================

rows = []

pdfs = sorted(
    PDF_FOLDER.glob("*.pdf")
)

pdfs = pdfs[:MAX_FILES]

print(
    f"{len(pdfs)} PDFs gefunden"
)

for i, pdf in enumerate(
    pdfs,
    start=1
):

    print(
        f"[{i}/{len(pdfs)}] "
        f"{pdf.name}"
    )

    text = extract_text(pdf)

    title = extract_title(pdf)

    year = extract_year(text)

    preview = (
        text[:500]
        .replace("\n", " ")
    )

    rows.append({

        "Originaldatei":
            pdf.name,

        "Erkannter_Titel":
            title,

        "Erkanntes_Jahr":
            year,

        "Textvorschau":
            preview

    })

df = pd.DataFrame(rows)

df.to_csv(
    OUTPUT_CSV,
    sep=";",
    encoding="utf-8-sig",
    index=False
)

print()
print(
    f"CSV gespeichert: "
    f"{OUTPUT_CSV}"
)

print(
    f"{len(df)} PDFs ausgewertet."
)
