#! /usr/bin/python3

from sys import argv
from PyPDF2 import PdfFileMerger
from os import listdir

if len(argv) != 3:
    print("ERROR: Wrong number of arguments.")
    print("Usage: " + argv[0] + " <pdf_directory> <name_of_merged_pdf>")
    exit(1)

print("Acquiring list of pdf files...")
pdfs = listdir(argv[1])
pdfs.sort()

char = ""

while char != "y" and char != "Y" and char != "n" and char != "N":
    print("Using this list of pdfs to merge in that order:")
    print(pdfs)
    print()
    char = input("Do you want to continue? [Y/N] ")

if char == "n" or char == "N":
    exit(0)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(argv[1] + "/" + pdf)

merger.write(argv[2])
merger.close()