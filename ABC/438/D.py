from collections import defaultdict, deque


def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]

	a_prefix_sum = [0]
	for i in a:
		a_prefix_sum.append(a_prefix_sum[-1] + i)
	b_prefix_sum = [0]
	for i in b:
		b_prefix_sum.append(b_prefix_sum[-1] + i)
	c_prefix_sum = [0]
	for i in c:
		c_prefix_sum.append(c_prefix_sum[-1] + i)

	bc_sum = defaultdict(lambda: float("-inf"))
	for i in range(1, n):
		bc_sum[b_prefix_sum[i] - c_prefix_sum[i] + c_prefix_sum[-1]] = max(
			bc_sum[b_prefix_sum[i] - c_prefix_sum[i] + c_prefix_sum[-1]], i - 1)

	bc_sum = deque(sorted(bc_sum.items(), reverse=True))

	result = float("-inf")
	for i in range(n - 2):
		tmp = a_prefix_sum[i + 1] - b_prefix_sum[i + 1]
		while bc_sum[0][1] <= i:
			bc_sum.popleft()
		result = max(result, tmp + bc_sum[0][0])

	print(result)


if __name__ == "__main__":
	main()
