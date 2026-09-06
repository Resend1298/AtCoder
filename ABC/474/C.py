def main():
	n, q = [int(i) for i in input().split()]
	p = [int(i) for i in input().split()]

	for _ in range(q):
		a = int(input())
		p.append(a)

	result = []
	result_set = set()
	for i in p[::-1]:
		if i not in result_set:
			result.append(i)
			result_set.add(i)

	print(*result[::-1])


if __name__ == "__main__":
	main()
