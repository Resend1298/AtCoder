def main():
	n = int(input())
	d = [int(i) for i in input().split()]

	location = [0]
	for i in d:
		location.append(location[-1] + i)

	for i in range(n - 1):
		tmp = []
		for j in range(i + 1, n):
			tmp.append(location[j] - location[i])
		print(*tmp)


if __name__ == "__main__":
	main()
