from sys import setrecursionlimit


def main():
	n, k = [int(i) for i in input().split()]

	if n == 1:
		print(k)
		exit()

	current = []
	setrecursionlimit(10 ** 7)

	def search(remaining, current_index):
		if current_index == n - 1:
			if remaining % (current_index + 1) == 0:
				current.append(remaining // (current_index + 1))
				print(*current)
				current.pop()
			return

		for i in range(remaining // (current_index + 1) + 1):
			current.append(i)
			search(remaining - i * (current_index + 1), current_index + 1)
			current.pop()

	for i in range(k + 1):
		current.append(i)
		search(k - i, 1)
		current.pop()


if __name__ == "__main__":
	main()
