# Will Taylor
# RouteCipher.py

'''
See README.md for description!
'''

def encodeRightLeftCipher(message, gridWidth):
	# ensure message fits in specified grid size
	if (len(message) > gridWidth**2):
		return "Please enter larger grid width!"
	encodeString = str(gridWidth)
	# make grid
	grid = makeGrid(gridWidth)
	gridLength = gridWidth**2
	extraChars = gridLength-len(message) 
	# determine wraparound chars and add to capitalized message string
	preEncode = addExtraChars(message.upper(),extraChars)
	# add to grid
	grid = fillEncodeGrid(grid, preEncode)
	# create encode string
	for r in range(gridWidth):
		if (r % 2 == 0):
			for i in grid[r][:]:
				encodeString += i
		elif (r % 2 == 1):
			for i in grid[r][::-1]:
				encodeString += i
	return encodeString

def decodeRightLeftCipher(encodedMessage):
	gridWidth = int((len(encodedMessage) - 1)**(0.5))
	grid = makeGrid(gridWidth)
	# remove number from character
	preDecode = encodedMessage[1::]
	# fill decode grid
	grid = fillDecodeGrid(grid, preDecode)
	# add all uppercase to final string
	decodedMessage = getStringWithUppers(grid)
	
	return decodedMessage

def make2dList(rows, cols):
	a = []
	for r in range(rows):
		a += [[0]*cols]
	return a

def makeGrid(gridWidth):
	return make2dList(gridWidth,gridWidth)

def addExtraChars(string, number):
	finalString = string
	alpha = ['a','b','c','d','e','f','g','h','i',
		'j','k','l','m','n','o','p','q','r',
		's','t','u','v','w','x','y','z']
	# range starts at 1 for reverse indexing
	for i in range(1, number+1):
		# add chars reverse alphabetically, rolling if > 26 needed 
		finalString += alpha[(i%26)*-1]
	return finalString

def fillEncodeGrid(grid, message):
	gridWidth = len(grid)
	# create position index counter for string
	pos = 0
	for col in range(gridWidth):
		for row in range(gridWidth):
			grid[row][col] = message[pos]
			pos += 1
	return grid

def fillDecodeGrid(grid, encodedMessage):
	gridWidth = len(grid)
	# create position index counter for string
	pos = 0
	maxIndex = gridWidth - 1
	for row in range(gridWidth):
		for col in range(gridWidth):
			if (row % 2 == 0):
				grid[row][col] = encodedMessage[pos]
				pos += 1
			elif (row % 2 == 1):
				grid[row][maxIndex - col] = encodedMessage[pos]
				pos += 1
	return grid

def getStringWithUppers(grid):
	gridWidth = len(grid)
	output = ""
	for col in range(gridWidth):
		for row in range(gridWidth):
			current = grid[row][col]
			if (current.isupper()):
				output += current
	return output

def testEncodeRLCipher():
	assert(encodeRightLeftCipher('weattackatdawn',4) == '4WTAWNTAEACDzyAKT')
	assert(encodeRightLeftCipher('topdowndesigniseffectiveforsolvinghardproblems',7)
		== '7TDSIOALERLVEEOPSFEVDMSPIFFIDOGEONRzyOGRCNWNITSHBx')
	assert(encodeRightLeftCipher('nlognisanefficientruntime',4) == 'Please enter larger grid width!')
	assert(encodeRightLeftCipher('nlognisanefficientruntime',6) == '6NSIREutzUCALONINysrxTEEGNFNIwqpvMTFI')
	print("All tests passed for encodeRightLeftCipher()!")

def testDecodeRLCipher():
	assert(decodeRightLeftCipher('4WTAWNTAEACDzyAKT') == 'WEATTACKATDAWN')
	assert(decodeRightLeftCipher('7TDSIOALERLVEEOPSFEVDMSPIFFIDOGEONRzyOGRCNWNITSHBx')
	 == 'TOPDOWNDESIGNISEFFECTIVEFORSOLVINGHARDPROBLEMS')
	assert(decodeRightLeftCipher('6NSIREutzUCALONINysrxTEEGNFNIwqpvMTFI') == 'NLOGNISANEFFICIENTRUNTIME')
	print("All tests passed for decodeRightLeftCipher()!")


testEncodeRLCipher()
testDecodeRLCipher()
