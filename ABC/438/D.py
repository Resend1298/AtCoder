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
	for i in range(n - 1):
		current_sum = b_prefix_sum[i + 1] + c_prefix_sum[-1] - c_prefix_sum[i + 1]
		bc_sum[current_sum] = max(bc_sum[current_sum], i)
	bc_sum = deque(sorted(bc_sum.items(), reverse=True))

	result = float("-inf")
	for i in range(n - 2):
		while bc_sum[0][1] <= i:
			bc_sum.popleft()
		current_sum = a_prefix_sum[i + 1] + bc_sum[0][0] - b_prefix_sum[i + 1]
		result = max(result, current_sum)

	print(result)


if __name__ == "__main__":
	main()
