# TODO: review

def main():
	n = int(input())

	result = 0
	for i in range(1, n + 1):
		result += (-1) ** i * i ** 3

	print(result)


if __name__ == "__main__":
	main()
