def bestTSP():
	# Open File
	file = open("test.in", "w")
	
	# Parse the values of the lines.
	nodeValues = []
	while file.readline():
		nodeValues.append(line)	
	numberofNodes = nodeValues[0]
	pattern = nodeValues[len(nodeValues) - 1]
	
	for node in range(0, numberofNodes):
		