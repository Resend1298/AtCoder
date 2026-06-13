def main():
	n = int(input())

	result = [[] for _ in range(n)]
	for i in range(n):
		a = [int(i) - 1 for i in input().split()]
		for j in a[1:]:
			result[j].append(i)

	for i in result:
		print(len(i), *[j + 1 for j in i])


if __name__ == "__main__":
	main()
