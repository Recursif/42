
listOfCsv = os.popen(findCommand).read()

listOfCsv = listOfCsv.split("\n")

print(listOfCsv)
