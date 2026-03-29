# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	current = [0] * m
	next_count = [0] * m
	for _ in range(n):
		a, b = [int(i) - 1 for i in input().split()]
		current[a] += 1
		next_count[b] += 1

	for i in range(m):
		print(next_count[i] - current[i])


if __name__ == "__main__":
	main()
