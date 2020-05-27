def proots():
	prime = int(input("Enter a prime number: "))
	num_to_check = 0
	p_minus_1_range = range(1,prime)
	print ("If you entered a large number (4+ digits) this could take a long time.")
	print ("")
	print ("Working...")
	primitive_roots = []
	for each in range(1, prime):
		num_to_check += 1
		candidate_prim_roots = []
		for i in range(1, prime):
			modulus = (num_to_check ** i) % prime
			candidate_prim_roots.append(modulus)
			cleanedup_candidate_prim_roots = set(candidate_prim_roots)
			if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
				primitive_roots.append(num_to_check)
	print ("Primitive roots of %d are:" % prime)
	print ("-----------------------------------")
	print (primitive_roots)
	print("Number of Total Primitive roots: ",len(primitive_roots))