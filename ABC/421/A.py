def main():
	n = int(input())
	s = [input() for _ in range(n)]
	x, y = input().split()
	x = int(x) - 1

	if s[x] == y:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
