from itertools import permutations


def main():
	n = int(input())
	p = [int(i) for i in input().split()]
	q = [int(i) for i in input().split()]

	result = 0

	for i in permutations(range(1, n + 1), n):
		for j in range(n):
			if p[j] > i[j]:
				break
			if p[j] < i[j]:
				for k in range(n):
					if i[k] > q[k]:
						break
					if i[k] < q[k]:
						result += 1
						break
				break

	print(result)


if __name__ == "__main__":
	main()
