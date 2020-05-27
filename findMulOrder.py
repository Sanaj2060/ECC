"""multiplicative order""" 

# funnction for GCD 
def GCD (a, b ) : 
	if (b == 0 ) : 
		return a 
	return GCD( b, a % b ) 

# Fucnction return smallest + ve 
# integer that holds condition 
# A ^ k(mod N ) = 1 
def multiplicativeOrder(A, N) : 
	if (GCD(A, N ) != 1) : 
		return -1

	# result store power of A that rised 
	# to the power N-1 
	result = 1

	K = 1
	while (K < N) : 
	
		# modular arithmetic 
		result = (result * A) % N 

		# return samllest + ve integer 
		if (result == 1) : 
			return K 

		# increment power 
		K = K + 1
	
	return -1

def findmulorder():
	# for all orders
	N = int(input("Enter the mod N: "))
	orders = []
	for i in range(1,N,1):
		order = multiplicativeOrder(i, N)
		if order != -1:
			orders.append([i,order])

	print(orders)

	choice = int(input("Enter 1 find the freq of specific order: "))
	if choice == 1:
		while(True):
			freq = 0
			x = int(input("Enter the Specific order: "))
			for i in orders:
				if i[1] == x:
					freq += 1
			print("The freq of the order is: ",freq)
