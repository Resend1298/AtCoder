def main():
	n, k, m = [int(i) for i in input().split()]
	gems = [[int(i) for i in input().split()] for _ in range(n)]

	gems = {(i, gems[i][0], gems[i][1]) for i in range(n)}

	colors = {}
	for i, c, v in gems:
		if c not in colors or v > colors[c][2]:
			colors[c] = (i, c, v)

	colors = sorted(colors.values(), key=lambda x: x[2], reverse=True)
	result = 0
	for i in range(m):
		result += colors[i][2]
		gems.remove(colors[i])

	k -= m
	gems = sorted(gems, key=lambda x: x[2], reverse=True)
	for i in range(k):
		result += gems[i][2]

	print(result)


if __name__ == "__main__":
	main()
