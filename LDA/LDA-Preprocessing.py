import os 

directory = "/home/171070030/Documents/Final year project/DATA/Sample100"
counter = 0
concatenatedFiles = ""
for root, dirnames, filenames in os.walk(directory):
	for fileName in filenames:
		filePath = directory + '/' + fileName
		name,ext = os.path.splitext(fileName)
		textDocument = open(filePath).read()
		textDocument = textDocument.replace("\"","")
		textDocument = textDocument.replace("\'","")
		if counter==99:
			concatenatedFiles = concatenatedFiles  + "\"" + textDocument + "\""
		else:
			concatenatedFiles = concatenatedFiles  + "\"" + textDocument + "\","
		print(counter)
		counter = counter+1

file1 = open("try.txt","w")
file1.write(concatenatedFiles)
file1.close()

