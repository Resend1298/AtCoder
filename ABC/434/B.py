# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	sizes = [[] for _ in range(m)]
	for _ in range(n):
		a, b = [int(i) for i in input().split()]
		sizes[a - 1].append(b)

	for i in sizes:
		print(sum(i) / len(i))


if __name__ == "__main__":
	main()
