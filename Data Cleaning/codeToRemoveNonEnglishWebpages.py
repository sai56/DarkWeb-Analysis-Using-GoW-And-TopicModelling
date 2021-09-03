import os
from nltk.corpus import stopwords
from langdetect import detect
import unicodedata
import codecs   

directory = '/home/171070030/Documents/Final year project/DATA/CleanedData'
onlyEnglishContentDirectory = '/home/171070030/Documents/Final year project/DATA/CleanedDataEnglish'
stopWords = set(stopwords.words('english'))
counter = 0



for root, dirnames, filenames in os.walk(directory):
    for directoryName in dirnames:
        directoryToExplore = directory + '/' + directoryName
        path = os.path.join(onlyEnglishContentDirectory, directoryName)
        os.mkdir(path)		
        for root, directroyNames, fileNames in os.walk(directoryToExplore):
            print(directoryName + " doing...")
            for fileName in fileNames:
                print(fileName+" doing... ")
                text = open(directoryToExplore+'/'+fileName, encoding="utf-8", errors='ignore').read()
                if(len(text)>10):
                    if(detect(text)=='en'):
                        infile = codecs.open(directoryToExplore+'/'+fileName,'r',encoding='ascii',errors='ignore')
                        outfile = codecs.open(path+'/'+fileName,'w',encoding='ascii',errors='ignore')
                        for line in infile.readlines():
                            for word in line.split():
                                if word not in stopWords:
                                    outfile.write(word+" ")
                        infile.close()
                        outfile.close()
                    else:
                        counter = counter+1
        

print("Total non english content files: "+ str(counter))


