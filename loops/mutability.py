filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)  # change first occurrence of '.' with '-'
    print(filename)

