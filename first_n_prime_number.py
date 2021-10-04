def prime(x):
	candidate = 2

	while x != 0:

		flag = True
		
		for i in range(2, candidate):
			if candidate % i == 0:
				flag = False
				break

		if flag:
			print(candidate)
			x -= 1

		candidate += 1

prime(5)

		