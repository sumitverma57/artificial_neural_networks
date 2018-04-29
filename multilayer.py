import math
#make prediction with weights
def predict(row,row1):
	activation=0.0
	Zin=0.0
	for i in range(len(row)):
		Zin+=row1[i]*row[i]
	Zin+=row1[-1]
	print("Zin=%f" %(Zin))
	activation=1/(1+math.exp(-Zin))
	return activation

def errinput(delta,row,din):
	for i in range(len(row)-1):
		din.append(row[i]*delta)
	return din

def updateweight(row,alpha,delta,z):
	for i in range(len(row)-1):
		row[i]=row[i]+alpha*delta*z[i]
	row[-1]=row[-1]+alpha*delta
	return row



#test predictions
x=[[0.6,0.8,0.0]]
alpha=1.0
weights=[[2.0,1.0,0.0,0.0],[1.0,2.0,3.0,0.0],[0.0,2.0,1.0,-1.0]]
#b=[0,0,-1]
z=[]
t=0.7
for row in x:
	for row1 in weights:
		prediction=predict(row,row1)
		print("Z=%f" %(prediction))
		z.append(prediction)
weight=[[-1,1,2,-1]]
for row1 in weight:
	y=predict(z,row1)
print("Y=%f" %(y))

count=1
while(y!=t):
	#error at response layer
	print("Error at response layer")
	delta=(t-y)*y*(1-y)
	print(delta)
	#error input to hidden layer
	din=[]
	for row in weight:
		din=errinput(delta,row,din)
	print(din)
	#error at hidden layer
	err=[]
	print("Error at hidden layer")
	for i in range(len(din)):
		err.append(din[i]*z[i]*(1-z[i]))
	print(err)
	#weight updation between hidden and response layer
	print("Weight updation between hidden and response layer")
	for row in weight:
		weight=[updateweight(row,alpha,delta,z)]
	print(weight)
	#weight updation between hidden and input layer
	print("Weight updation between hidden and input layer")
	e=0
	for row in weights:
		for i in range(len(row)-1):
			row[i]=row[i]+alpha*err[e]*x[0][i]
		row[i+1]+=alpha*err[e]
		e+=1
	print(weights)
	
	print "\n--------------------------------------\n"
	z=[]
	for row in x:
		for row1 in weights:
			prediction=predict(row,row1)
			print("Z=%f" %(prediction))
			z.append(prediction)
	
	for row1 in weight:
		y=predict(z,row1)
	print("Y=%f" %(y))

	count+=1
print(count)
