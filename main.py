import pandas
import os
import glob
from fpdf import FPDF
from termcolor import colored


csv_files = glob.glob(os.path.join("C:\\Users\\HP\\Downloads\\csv_files", "*.csv"))

main_data={}
for file_loc in csv_files:
    x = pandas.read_csv(file_loc)
    li = []
    for col in x.columns:
        li.append(col)
    index = {}
    for column in x:
        index[column] = set(x[column].values)
    main_data[file_loc] = index

with open("main_converted.rtf", mode="w") as f:
    for file_data in main_data:
        space = 0
        f.write(file_data)
        space+=len(str(file_data))
        f.write("\n\n")
        for i in main_data[file_data]:
            f.write(f"{i}: ")
            space+=len(str(i))
            space+=2
            for j in main_data[file_data][i]:
                f.write(f"{j}; ")
                space+=len(str(j))
                space+=2
                if space>150:
                    f.write("\n")
                    space = 0
            f.write('\n\n')
        f.write("\n\n\n\n\n")



pdf = FPDF(orientation="L", format="A3")
pdf.add_page()
pdf.set_font("Arial", size=10)
f = open("main_converted.rtf", 'r')
for z in f.readlines():
    pdf.cell(10, 10, txt = z, ln = 1)
pdf.output("main_converted.pdf")