import boto3
def printFunctionChange(found, data,f, path):
	for i in range(0,found+1):
		if i == found:
			with open(path, 'r') as q:
				for line in q:
					f.write(line)
		f.write(data[i])
		
		
retrievedValue = 0;
path = 'C:\Users\Jordan\Documents\Hackathon\Assets\AWSScript.cs'
count = 0
found = 0
data = []
with open(path, 'r') as f:
	for line in f:
		if "//Badgers" in line:
			found = count
		else:
			data.append(line)
			if count >= 23:
				break
		count += 1;
with open(path, 'w') as f:
	textPath = ''
	if retrievedValue == 0:
		textPath = 'spawnCube.txt'
	elif retrievedValue == 1:
		textPath = 'addTexture.txt'
	elif retrievedValue == 2:
		textPath = 'addSurroudings.txt'
	else: 
		textPath = 'startMovie.txt'
	printFunctionChange(found, data,f, textPath)
			
			

