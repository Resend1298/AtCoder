def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	k = int(input())

	result = 0
	for i in a:
		if k <= i:
			result += 1

	print(result)


if __name__ == "__main__":
	main()
