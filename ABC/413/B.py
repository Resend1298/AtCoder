def main():
	n = int(input())
	s = [input() for _ in range(n)]

	result = set()
	for i in s:
		for j in s:
			if i != j:
				result.add(i + j)

	print(len(result))


if __name__ == "__main__":
	main()
