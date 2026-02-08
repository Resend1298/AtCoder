# TODO: review

def digit_sum(x):
	return sum(int(i) for i in str(x))


def main():
	n, k = [int(i) for i in input().split()]

	result = 0

	for i in range(1, n + 1):
		if digit_sum(i) == k:
			result += 1

	print(result)


if __name__ == "__main__":
	main()
