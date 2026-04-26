# TODO: review

def main():
	n, q = [int(i) for i in input().split()]

	father = [i for i in range(n)]
	top = set(i for i in range(n))

	for _ in range(q):
		c, p = [int(i) - 1 for i in input().split()]

		if father[c] != c:
			top.add(father[c])
		father[c] = p
		top.remove(p)

	result = [0] * n
	for i in top:
		result_tmp = 1
		while father[i] != i:
			i = father[i]
			result_tmp += 1
		result[i] = result_tmp

	print(*result)


if __name__ == "__main__":
	main()
