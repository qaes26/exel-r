import sys
import subprocess

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

# Read PDF
try:
    reader = pypdf.PdfReader('c:\\Users\\طلال ابو قيس\\Desktop\\rahaf exel\\Excel part 1.pdf')
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    
    with open('c:\\Users\\طلال ابو قيس\\Desktop\\rahaf exel\\extracted_pdf.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(text))
    print("PDF extraction complete.")
except Exception as e:
    print(f"Error extracting PDF: {e}")
