def solve(m, factorial_table):
	n = int(input())
	c = [int(i) for i in input().split()]

	c_sum = sum(c)

	if c_sum > len(factorial_table) - 1:
		for i in range(len(factorial_table), c_sum + 1):
			factorial_table.append(factorial_table[-1] * i)

	result = factorial_table[c_sum]

	for i in c:
		result //= factorial_table[i]

	print(result % m)


def main():
	t, m = [int(i) for i in input().split()]

	factorial_table = [0, 1]

	for _ in range(t):
		solve(m, factorial_table)


if __name__ == "__main__":
	main()
