def main():
	n, k, m = [int(i) for i in input().split()]
	cv = [[int(i) for i in input().split()] for _ in range(n)]

	gems = {(i, cv[i][0], cv[i][1]) for i in range(n)}
	result = 0

	most_valuable_by_color = {}
	for i, c, v in gems:
		if c not in most_valuable_by_color or v > most_valuable_by_color[c][2]:
			most_valuable_by_color[c] = (i, c, v)
	most_valuable_by_color = sorted(most_valuable_by_color.values(), key=lambda x: x[2], reverse=True)
	for i in range(m):
		result += most_valuable_by_color[i][2]
		gems.remove(most_valuable_by_color[i])
	k -= m

	gems = sorted([i[2] for i in gems], reverse=True)
	result += sum(gems[:k])

	print(result)


if __name__ == "__main__":
	main()
