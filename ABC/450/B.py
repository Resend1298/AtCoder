def main():
	n = int(input())
	cost = [[int(i) for i in input().split()] for _ in range(n - 1)]

	for a in range(n - 2):
		for b in range(a + 1, n - 1):
			for c in range(b + 1, n):
				if cost[a][c - a - 1] > cost[a][b - a - 1] + cost[b][c - b - 1]:
					print("Yes")
					exit()

	print("No")


if __name__ == "__main__":
	main()
