from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()

path_to_files = r'PdfsToMerge/'

for root, dirs, file_names in os.walk(path_to_files):
    for file_name in file_names:
        merger.append(path_to_files + file_name)

#Write out the merged PDF
merger.write("merged.pdf")
merger.close()