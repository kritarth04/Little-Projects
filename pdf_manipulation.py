from pypdf import PdfReader,PdfMerger,PdfWriter

def read():
    read = PdfReader("D:/VS Code Files/Coding Practices/pdf/Unit 1 - Mathematics III - www.rgpvnotes.in.pdf")
    pages = len(read.pages)
    page = read.pages[1]
    text = page.extract_text()
    print(text)

def merge():
    merger = PdfWriter()

    for pdf in ["D:/VS Code Files/Coding Practices/pdf/Unit 1 - Mathematics III - www.rgpvnotes.in.pdf","D:/VS Code Files/Coding Practices/pdf/Unit 2 - Mathematics III - www.rgpvnotes.in.pdf", "D:/VS Code Files/Coding Practices/pdf/Unit 3 - Mathematics III - www.rgpvnotes.in.pdf"]:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()

read()
merge()
