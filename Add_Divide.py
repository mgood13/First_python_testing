def main():
	sum = add_three(15, 2, 31)
	divide_by_three(sum)

def add_three(v1, v2, v3):
	"""This function adds three numbers together
	:param v1: First number
	:param v2: Second number
	:param v3: Thirds number
	"""

	p = v1 + v2 + v3
	return p

def divide_by_three(v1):
	"""This function divides a number by 3
	:param v1: First Number
	:returns: product number
	"""

	p = v1/3
	return p


if __name__ == "__main__":
	main()
