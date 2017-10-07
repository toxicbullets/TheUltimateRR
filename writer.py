import boto3
def printFunction(found, data,f ):
	data[found] = "		GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);\n cube.transform.position = new Vector3(0, 0.5F, 0);\n //Badgers\n}}"
	for i in range(0,found+1):
		f.write(data[i])
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
	printFunction(found, data,f )
			
			

