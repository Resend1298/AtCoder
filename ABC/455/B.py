def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	result = 0
	for h1 in range(h):
		for h2 in range(h1, h):
			for w1 in range(w):
				for w2 in range(w1, w):
					if all(s[i][j] == s[h1 + h2 - i][w1 + w2 - j] for i in range(h1, h2 + 1) for j in
					       range(w1, w2 + 1)):
						result += 1

	print(result)


if __name__ == "__main__":
	main()
