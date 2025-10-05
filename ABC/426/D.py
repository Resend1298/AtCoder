# TODO: review

def solve():
	n = int(input())
	s = [int(i) for i in list(input())]

	if all(i == 0 for i in s) or all(i == 1 for i in s):
		print(0)
		return

	cost_from_left = []
	cost_from_right = []
	count_0 = 0
	count_1 = 0
	for i in range(n):
		if s[i] == 0:
			count_0 += 1
			continue
		count_1 += 1
		cost_from_left.append(2 * count_0 + count_1)
	count_0 = 0
	count_1 = 0
	for i in range(n - 1, -1, -1):
		if s[i] == 0:
			count_0 += 1
			continue
		count_1 += 1
		cost_from_right.append(2 * count_0 + count_1)
	result_0 = min(cost_from_left[-1], cost_from_right[-1])
	for i in range(len(cost_from_right) - 1):
		result_0 = min(result_0, cost_from_left[-1 - i - 1] + cost_from_right[i])

	cost_from_left = []
	cost_from_right = []
	count_0 = 0
	count_1 = 0
	for i in range(n):
		if s[i] == 1:
			count_1 += 1
			continue
		count_0 += 1
		cost_from_left.append(2 * count_1 + count_0)
	count_0 = 0
	count_1 = 0
	for i in range(n - 1, -1, -1):
		if s[i] == 1:
			count_1 += 1
			continue
		count_0 += 1
		cost_from_right.append(2 * count_1 + count_0)
	result_1 = min(cost_from_left[-1], cost_from_right[-1])
	for i in range(len(cost_from_right) - 1):
		result_1 = min(result_1, cost_from_left[-1 - i - 1] + cost_from_right[i])

	print(min(result_0, result_1))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
