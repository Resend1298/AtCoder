from math import comb


def main():
	n = int(input())
	p = [int(i) - 1 for i in input().split()]

	next_ = [-1] * n
	for i in range(n):
		next_[i] = p[i]

	result = 0
	visited = [False] * n

	for i in range(n):
		if visited[i]:
			continue

		current = i
		visited[i] = True
		loop_len = 1

		while next_[current] != i:
			current = next_[current]
			visited[current] = True
			loop_len += 1

		result += comb(loop_len, 2)

	print(result)


if __name__ == "__main__":
	main()
