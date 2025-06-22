def main():
	n = int(input())
	d = [int(i) for i in input().split()]

	location = [0]
	for i in d:
		location.append(location[-1] + i)

	for i in range(n - 1):
		print(*[location[j] - location[i] for j in range(i + 1, n)])


if __name__ == "__main__":
	main()
