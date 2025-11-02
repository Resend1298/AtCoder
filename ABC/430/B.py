# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	s = [input() for _ in range(n)]

	result = set()

	for i in range(n - m + 1):
		for j in range(n - m + 1):
			tmp = []
			for k in range(m):
				for l in range(m):
					tmp.append(s[i + k][j + l])
			result.add(''.join(tmp))

	print(len(result))


if __name__ == "__main__":
	main()
