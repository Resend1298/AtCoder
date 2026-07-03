def main():
	n = int(input())
	a = [[int(i) for i in input().split()] for _ in range(n)]

	cost = [[float("inf")] * n for _ in range(2 ** n)]
	cost[0][0] = 0

	for visited in range(2 ** n):
		for current_location in range(n):
			for next_location in range(n):
				if not 2 ** next_location & visited:
					cost[visited | 2 ** next_location][next_location] = min(
						cost[visited | 2 ** next_location][next_location],
						cost[visited][current_location] + a[current_location][next_location])

	print(cost[-1][0])


if __name__ == "__main__":
	main()
