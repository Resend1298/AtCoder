# TODO: review

def main():
	n, v = [int(i) for i in input().split()]
	w = [int(i) for i in input().split()]

	result = float("-inf")

	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				if i + j + k + 3 <= v:
					result = max(result, w[i] + w[j] + w[k])

	print(result)


if __name__ == "__main__":
	main()
