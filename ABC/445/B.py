def main():
	n = int(input())
	s = [input() for _ in range(n)]

	m = max(len(i) for i in s)

	for i in s:
		k = (m - len(i)) // 2
		print('.' * k + i + '.' * k)


if __name__ == "__main__":
	main()
