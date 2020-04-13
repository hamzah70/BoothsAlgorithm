# Computer Organization (CSE-112) 
# Project - 2 : Booth's Algorithm for Multiplication and Division of Binary Numbers
# Submitted by : Hamzah Akhtar (2018051) and Shashwat Aggarwal (2018097)

def twosComplement(M):
	length = len(M)
	i = length - 1

	while(i>=0):
		if(M[i]=='1'):
			break
		i-=1

	if(i==-1):
		return M

	j = i-1
	number = M[i:]

	while(j>=0):
		if(M[j]=='1'):
			number = '0'+number
		else:
			number = '1'+number
		j-=1
	return number

def shiftRight(A, Q, q0, n):
	q0 = Q[n-1]

	finalA=A[0]
	for i in range(n-1):
		finalA=finalA+A[i]

	finalQ = A[n-1]
	for i in range(n-1):
		finalQ=finalQ+Q[i]

	return finalA, finalQ, q0

def shiftLeft(A,Q):
	A = A[1:] + Q[0]
	Q = Q[1:] + '0'
	return A,Q

def addBinaryNumber(a, b, n):

	result = ''
	carry = 0
	for i in range(n-1, -1, -1):
		currentBit = carry
		if(a[i]=='1'):
			currentBit+=1
		if(b[i]=='1'):
			currentBit+=1
		if(currentBit%2==0):
			result ='0' + result
		else:
			result ='1' + result
		if(currentBit<2):
			carry=0
		else:
			carry=1

	return result

def subtractBinaryNumber(x,y):
	y=twosComplement(y)
	return addBinaryNumber(x,y,len(x))

def multiply(M, minusM, Q, A, q0, n):
	length = n

	while(n!=0):
		
		q1q0 = Q[length-1]+q0

		if(q1q0=='10'):
			A = addBinaryNumber(A, minusM, length)
		elif(q1q0=='01'):
			A = addBinaryNumber(A, M, length)

		A, Q, q0 = shiftRight(A, Q, q0, length)
		n-=1

	answer = A+Q
	if(answer[0]=='0'):
		return(int(answer, 2),answer)
	else:
		ans = twosComplement(answer)
		
		return (-1) * int(ans, 2), answer

def divide(Q,M,q,m):
	n = len(q)
	a = '0'*(n+1)
	m = '0' + m
	A = 0

	while(n>0):
		a,q = shiftLeft(a,q)
		restoreA = a
		a = subtractBinaryNumber(a,m)
		if(a[0]=='1'):
			q= q[:-1] + '0'
			a = restoreA
		else:
			q = q[:-1] + '1'
		n-=1
	q = '0' + q
	
	if(Q<0):
		A = -(int(a,2))
		a = twosComplement(a)
	else:
		A = int(a,2)
	if(Q*M<0):
		Q = -(int(q,2))
		q = twosComplement(q)
	else:
		Q = int(q,2)
	print("\nBINARY:     Quotient = {:<15} Remainder = {:}".format(q,a))
	print("DECIMAL:    Quotient = {:<15} Remainder = {:} \n\n".format(Q,A))
	

def multiplication(x,y):
	Multiplier = int(x)
	Multiplicand = int(y)

	if(abs(Multiplier)<abs(Multiplicand)):
		Multiplier,Multiplicand = Multiplicand,Multiplier
	
	m = '0'+str(bin(abs(Multiplier)))[2:]
	q = '0'+str(bin(abs(Multiplicand)))[2:]

	short ='0'* (len(m)-len(q))
	q = short+q

	if Multiplier>=0:
		M = m
		minusM = twosComplement(m)
	else:
		M = twosComplement(m)
		minusM = m

	if Multiplicand >=0:
		Q = q
	else:
		Q = twosComplement(q)

	n = len(M)
	A = '0'*n
	q0 = '0'

	decimalProduct, binaryProduct = multiply(M, minusM, Q, A, q0, n)
	print(str(x)+"*"+str(y))
	print("\nBINARY:		Product = " + binaryProduct)
	print("DECIMAL:	Product = " + str(decimalProduct) + "\n\n")

def division(x,y):
	x = int(x)
	y = int(y)

	binaryX = bin(abs(x))[2:]
	binaryY = bin(abs(y))[2:]
	if(len(binaryX)>len(binaryY)):
		binaryY = '0'*(len(binaryX)-len(binaryY)) + binaryY
	else:
		binaryX = '0'*(len(binaryY)-len(binaryX)) + binaryX
	print(str(x)+"/"+str(y))
	if(y!=0):
		divide(x,y,binaryX,binaryY)
	else:
		print("Invalid division! Cannot divide by 0 \n\n")

if __name__ == "__main__":
	
	with open("testcases.txt", 'r') as f:
		for line in f:
			x,y=line.split()
			multiplication(x,y)
			division(x,y)
	# option = 'x'
	# while(option != '3'):
	# 	print("BOOTH'S ALGORITHM FOR MULTIPLICATION AND DIVISION OF BINARY NUMBERS")
	# 	print("1. Multiplication\t2. Division\t3. Exit")
	# 	option = input()
	# 	if(option == '2'):
	# 		division()
	# 	elif(option == '1'):
	# 		multiplication()
	# 	elif(option=='3'):
	# 		print("Exiting")
	# 	else:
	# 		print("Select correct option!")
