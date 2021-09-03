import os 
import re
from bs4 import BeautifulSoup
from bs4.element import Comment

directory = '/home/171070030/Documents/Final year project/DATA/chakra/ProjectChakravyuh/src/media/crawled'
cleanDataDirectory = '/home/171070030/Documents/Final year project/DATA/CleanedData'
counter = 0

def getRawHtml(filePath):
	str = """"""
	with open(filePath) as report_file:
    		raw_html = report_file.readlines()
    		str = """""".join(raw_html)
	return str


def tagVisible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def textFromHtml(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visibleTexts = filter(tagVisible, texts)  
    return u" ".join(t.strip() for t in visibleTexts)

def extractTextFromHtml(filePath,path,fileName):

	rawHtml = getRawHtml(filePath)
	cleantext = textFromHtml(rawHtml)
	finaltext0 = re.sub(' +', ' ', cleantext)
	finaltext1 = re.sub('\n','',finaltext0)

	if(len(finaltext1)<=1):
		return False
	textFilePath = os.path.join(path, fileName+".txt")
	fileToWrite = open(textFilePath, "w")
	fileToWrite.write(finaltext1.encode('utf-8'))
	fileToWrite.close()
	return True


for root, dirnames, filenames in os.walk(directory):
	for directoryName in dirnames:
		directoryToExplore = directory + '/' + directoryName
		path = os.path.join(cleanDataDirectory, directoryName)
		os.mkdir(path)		
		for root, directroyNames, fileNames in os.walk(directoryToExplore):
			for fileName in fileNames:
				if(fileName.endswith('.html') or fileName.endswith('.php') or fileName.endswith('.htm')):
					filePath = directoryToExplore + '/' + fileName
					name, ext = os.path.splitext(fileName)
					if(extractTextFromHtml(filePath,path,name)):
						counter = counter+1
		print(directoryName + " done...")

print("Total txt files generated: " + str(counter))

				
