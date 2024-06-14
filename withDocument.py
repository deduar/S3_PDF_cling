import os
import shutil

file1 = open('Cling_result.txt', 'r')

for line in file1:
    if "documentUrl" in line and "pdf" in line:
        if len(line.strip().split("/")) > 8:
            print(line.strip().split("/")[9].split(".pdf")[0])
            shutil.copy("PDF/"+line.strip().split(
                "/")[9].split(".pdf")[0]+".pdf", "DOS")
