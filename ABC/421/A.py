def main():
	n = int(input())
	s = [input() for _ in range(n)]
	x, y = input().split()
	x = int(x) - 1

	print("Yes" if s[x] == y else "No")


if __name__ == "__main__":
	main()
