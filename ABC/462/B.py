def main():
	n = int(input())
	ka = [[int(i) - 1 for i in input().split()] for _ in range(n)]

	result = [[] for _ in range(n)]
	for i in range(n):
		for j in ka[i][1:]:
			result[j].append(i)

	for i in range(n):
		print(len(result[i]), *[j + 1 for j in result[i]])


if __name__ == "__main__":
	main()
