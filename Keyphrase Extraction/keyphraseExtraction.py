import pke
import os


def extractKeyphrases(fileName):
	
	print(fileName)
	# initialize keyphrase extraction model, here TopicRank
	extractor = pke.unsupervised.TopicRank()

	# load the content of the document, here document is expected to be in raw
	# format (i.e. a simple text file) and preprocessing is carried out using spacy
	extractor.load_document(input=fileName)

	# keyphrase candidate selection, in the case of TopicRank: sequences of nouns
	# and adjectives (i.e. `(Noun|Adj)*`)
	extractor.candidate_selection()

	# candidate weighting, in the case of TopicRank: using a random walk algorithm
	extractor.candidate_weighting()

	# N-best selection, keyphrases contains the 10 highest scored candidates as
	# (keyphrase, score) tuples
	keyphrases = extractor.get_n_best(n=4)

	return keyphrases

directory = "combined/"
orderingDirectory = "orderedFiles/"
counter = 1
file1 = open("output.txt","w")

for root, dirnames, filenames in os.walk(directory):
	for fileName in filenames:
		kp = extractKeyphrases(directory+fileName)
		fileToWrite = open(orderingDirectory+str(counter)+'.txt',"w+")
		fileContent = open(directory+fileName,"r")
		fileToWrite.write(fileContent.read())
		if(len(kp)==4):
			text = str(counter)+','+kp[0][0]+','+kp[1][0]+','+kp[2][0]+','+kp[3][0]+'\n'
		elif(len(kp)==3):
			text = str(counter)+','+kp[0][0]+','+kp[1][0]+','+kp[2][0]+'\n'
		elif(len(kp)==2):
			text = str(counter)+','+kp[0][0]+','+kp[1][0]+'\n'
		elif(len(kp)==1):
			text = str(counter)+','+kp[0][0]+'\n'
		else:
			text = str(counter)+',NKP'+'\n'
			
		counter = counter+1
		file1.write(text)
		fileToWrite.close()
		fileContent.close()
file1.close()				


