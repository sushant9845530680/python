from PyPDF2 import PdfWriter
f=PdfWriter()
pdfs=[]

n=int(input("Enter the number of pdfs:"))
for i in range(n):
    name=input(f"Enter the name of pdf {i+1}:")
    pdfs.append(name)

for pdf in pdfs:
    f.append(pdf)

f.write("merged.pdf")
f.close()