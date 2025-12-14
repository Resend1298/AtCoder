# TODO: review

def main():
	n = int(input())
	p = [int(i) for i in input().split()]

	result = 0
	visited = [False] * n

	for i in range(n):
		if i + 1 == p[i] or visited[i]:
			continue

		cycle_length = 1
		current = i
		while p[current] != i + 1:
			visited[current] = True
			current = p[current] - 1
			cycle_length += 1
		visited[current] = True

		result += cycle_length * (cycle_length - 1) // 2

	print(result)


if __name__ == "__main__":
	main()
