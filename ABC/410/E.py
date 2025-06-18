# TODO: review

def main():
	n, h, m = [int(i) for i in input().split()]
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	current = {h: m}

	for i in range(n + 1):
		if i == n:
			print(n)
			exit()

		new = {}
		for j, k in current.items():
			if j >= ab[i][0]:
				if j - ab[i][0] in new:
					new[j - ab[i][0]] = max(new[j - ab[i][0]], k)
				else:
					new[j - ab[i][0]] = k
			if k >= ab[i][1]:
				if j in new:
					new[j] = max(new[j], k - ab[i][1])
				else:
					new[j] = k - ab[i][1]

		if not new:
			print(i)
			exit()

		current = new


if __name__ == "__main__":
	main()
