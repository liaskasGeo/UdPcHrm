files_names = ["1.Raw Data.txt","2.Reports.txt","3.Presentations.txt"]
for filename in files_names:
    print(filename)

print("===================================================================")

for filename in files_names:
    filename = filename.replace(".","-") #changes all the dots with underscores
    print(filename)

print("===================================================================")

for filename in files_names:
    filename = filename.replace(".","-",1)  # changes only the first dot
    print(filename)


print(files_names)



