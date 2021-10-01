def prime(x):
	counter = 0

	candidate = 2

	while counter != x:

		flag = True
		
		for i in range(2, candidate):
			if candidate % i == 0:
				flag = False
				break

		if flag:
			print(candidate)
			counter += 1

		candidate += 1

prime(5)

		