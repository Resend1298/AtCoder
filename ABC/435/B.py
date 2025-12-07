# TODO: review

def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	result = 0
	for l in range(n):
		for j in range(l, n):
			sum_lj = sum(a[l:j + 1])
			for i in a[l:j + 1]:
				if sum_lj % i == 0:
					break
			else:
				result += 1

	print(result)


if __name__ == "__main__":
	main()
