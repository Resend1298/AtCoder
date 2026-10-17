def main():
	n, m = [int(i) for i in input().split()]
	s = [input() for _ in range(n)]
	t = [input() for _ in range(m)]

	result = [0] * n
	name_to_id = {name: i for i, name in enumerate(s)}

	for i in t:
		if i in name_to_id:
			result[name_to_id[i]] += 1
			continue

		possible = []
		for name, j in name_to_id.items():
			if len(i) == len(name) and sum(1 for a, b in zip(i, name) if a != b) == 1:
				possible.append(j)

		if len(possible) == 1:
			result[possible[0]] += 1

	for i in result:
		print(i)


if __name__ == "__main__":
	main()
