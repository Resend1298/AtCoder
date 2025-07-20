# TODO: review

def main():
	h, w = [int(i) for i in input().split()]
	a = [[int(i) for i in input().split()] for _ in range(h)]
	p = [int(i) for i in input().split()]

	necessary = [[0] * w for _ in range(h)]

	for i in range(h - 1, -1, -1):
		for j in range(w - 1, -1, -1):
			tmp = p[i + j] - a[i][j]
			if i < h - 1 and j < w - 1:
				tmp += max(min(necessary[i + 1][j], necessary[i][j + 1]), 0)
			elif i < h - 1:
				tmp += max(necessary[i + 1][j], 0)
			elif j < w - 1:
				tmp += max(necessary[i][j + 1], 0)
			necessary[i][j] = tmp

	necessary[0][0] = max(0, necessary[0][0])
	# if p[0] > a[0][0]:
	# 	necessary[0][0] += p[0] - a[0][0]
	print(necessary[0][0])


if __name__ == "__main__":
	main()
