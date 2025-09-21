# TODO: review

def main():
	n, m, k = [int(i) for i in input().split()]
	count = [m] * n
	result = []
	for _ in range(k):
		a, b = [int(i) - 1 for i in input().split()]
		count[a] -= 1
		if count[a] == 0:
			result.append(a + 1)
	print(*result)


if __name__ == "__main__":
	main()
