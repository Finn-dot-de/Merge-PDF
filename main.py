import os
import re
import PyPDF2

def get_pdf_files():
    """Searches for all PDF files in the current directory."""
    return [f for f in os.listdir() if f.endswith(".pdf")]

def sort_numerically_or_alphabetically(files):
    """Sorts the files numerically if possible, otherwise alphabetically."""
    def extract_number(file):
        match = re.search(r'\d+', file)  # Search for numbers in the filename
        return int(match.group()) if match else float('inf')
    
    return sorted(files, key=lambda x: (extract_number(x), x))

def merge_pdfs(pdf_files, output_filename="merged.pdf"):
    """Merges the PDF files in the specified order."""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_files:
        try:
            merger.append(pdf)
            print(f"Adding: {pdf}")
        except Exception as e:
            print(f"Error processing {pdf}: {e}")
    
    if pdf_files:
        merger.write(output_filename)
        merger.close()
        print(f"Merged file saved as: {output_filename}")
    else:
        print("No PDF files found.")

def main():
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    sorted_pdfs = sort_numerically_or_alphabetically(pdf_files)
    merge_pdfs(sorted_pdfs)

if __name__ == "__main__":
    main()
