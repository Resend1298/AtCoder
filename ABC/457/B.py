def main():
	n = int(input())
	a = [[int(i) for i in input().split()] for _ in range(n)]
	x, y = [int(i) - 1 for i in input().split()]

	print(a[x][y + 1])


if __name__ == "__main__":
	main()
