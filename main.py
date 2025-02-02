import os
import re
import PyPDF2

def get_pdf_files():
    """Sucht nach allen PDF-Dateien im aktuellen Verzeichnis."""
    return [f for f in os.listdir() if f.endswith(".pdf")]

def sort_numerically_or_alphabetically(files):
    """Sortiert die Dateien numerisch, falls möglich, ansonsten alphabetisch."""
    def extract_number(file):
        match = re.search(r'\d+', file)  # Suche nach Zahlen im Dateinamen
        return int(match.group()) if match else float('inf')
    
    return sorted(files, key=lambda x: (extract_number(x), x))

def merge_pdfs(pdf_files, output_filename="zusammengefuegt.pdf"):
    """Führt die PDF-Dateien in der angegebenen Reihenfolge zusammen."""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_files:
        try:
            merger.append(pdf)
            print(f"Füge hinzu: {pdf}")
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {pdf}: {e}")
    
    if pdf_files:
        merger.write(output_filename)
        merger.close()
        print(f"Zusammengeführte Datei gespeichert als: {output_filename}")
    else:
        print("Keine PDF-Dateien gefunden.")

def main():
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        print("Keine PDF-Dateien im aktuellen Verzeichnis gefunden.")
        return
    
    sorted_pdfs = sort_numerically_or_alphabetically(pdf_files)
    merge_pdfs(sorted_pdfs)

if __name__ == "__main__":
    main()
