# TODO: review

def main():
	n, m = [int(i) for i in input().split()]

	result = 0
	while m != 0:
		m = n % m
		result += 1

	print(result)


if __name__ == "__main__":
	main()
