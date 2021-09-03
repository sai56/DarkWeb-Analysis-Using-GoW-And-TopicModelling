import os
import networkx as nx
import string
from sys import maxsize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 


def constructGraph(filePath, fileName, counter):
	#print(filePath)
	textDocument = open(filePath).read()

	wordList1 = textDocument.split()
	wordList2 = [str.rstrip(x.lower(), ',.!?;') for x in wordList1]
	wordList3 = []	
	for word in wordList2:
		if len(word)>=3:
			wordList3.append(word)

	dG = nx.DiGraph()

	for i, word in enumerate(wordList3):
    		try:
        		next_word = wordList3[i + 1]
        		if not dG.has_node(word):
            			dG.add_node(word)
            			dG.nodes[word]['count'] = 1
        		else:
            			dG.nodes[word]['count'] += 1
        		if not dG.has_node(next_word):
            			dG.add_node(next_word)
            			dG.nodes[next_word]['count'] = 0

        		if not dG.has_edge(word, next_word):
            			dG.add_edge(word, next_word, weight=1)
        		else:
            			dG.adj[word][next_word]['weight'] += 1
    		except IndexError:
        		if not dG.has_node(word):
            			dG.add_node(word)
            			dG.nodes[word]['count'] = 1
       			else:
            			dG.nodes[word]['count'] += 1
    		except:
        		raise

	listOfNodes = []
	#edgeColorList = []

	for node in dG.nodes():
    		if(dG.nodes[node]['count']==1):
        		listOfNodes.append(node)    

	dG.remove_nodes_from(listOfNodes)
	return dG.nodes()

	#for edge in dG.edges():
    	#	if(dG.adj[edge[0]][edge[1]]['weight']==1):
        #		edgeColorList.append('black')
    	#	else:
        #		edgeColorList.append('red')

	#f = plt.figure()
	#nx.draw_random(dG,edge_color = edgeColorList, node_color = 'yellow',with_labels=True)
	#f.savefig("GoW"+str(counter)+".png")


directory = "/home/171070030/Documents/Final year project/DATA/Sample1"
counter = 0
GoWNodesArrays = []

for root, dirnames, filenames in os.walk(directory):
	for fileName in filenames:
		filePath = directory + '/' + fileName
		name,ext = os.path.splitext(fileName)
		nodes = constructGraph(filePath,name,counter)
		#print(nodes)
		text = ""
		for node in nodes:
			text = text+node+" "
		print(text)		
		GoWNodesArrays.append(nodes)
		counter = counter+1

#print(GoWNodesArrays)
