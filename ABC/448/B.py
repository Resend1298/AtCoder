# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	result = 0

	for a, b in ab:
		result += min(b, c[a - 1])
		c[a - 1] -= min(b, c[a - 1])

	print(result)


if __name__ == "__main__":
	main()
