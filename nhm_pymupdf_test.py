from pathlib import Path

pdf_folder = Path("test_pdfs")

print("Aktuelles Verzeichnis:")
print(Path.cwd())

print("\nOrdner existiert:")
print(pdf_folder.exists())

print("\nInhalt:")

for f in pdf_folder.iterdir():
    print(f.name)

pdfs = list(pdf_folder.glob("*.pdf"))

print("\nPDFs gefunden:")
print(len(pdfs))

for pdf in pdfs:
    print(pdf.name)
