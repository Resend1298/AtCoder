def main():
	n = int(input())
	a = [[int(i) for i in input().split()] for _ in range(n - 1)]

	result = float("-inf")

	for group_1 in range(2 ** n):
		for group_2 in range(2 ** n):
			if group_1 & group_2:
				continue

			group_3 = 2 ** n - 1 - (group_1 | group_2)

			current_result = 0
			for i in range(n - 1):
				for j in range(i + 1, n):
					if (((2 ** i & group_1) and (2 ** j & group_1))
							or ((2 ** i & group_2) and (2 ** j & group_2))
							or ((2 ** i & group_3) and (2 ** j & group_3))):
						current_result += a[i][j - i - 1]
			result = max(result, current_result)

	print(result)


if __name__ == "__main__":
	main()
