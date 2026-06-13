from math import comb


def main():
	n, d = [int(i) for i in input().split()]
	st = [[int(i) for i in input().split()] for _ in range(n)]

	st = [[s, t - d] for s, t in st if s + d <= t]
	if not st:
		print(0)
		exit()
	start = min(i[0] for i in st)
	st = [[s - start, t - start] for s, t in st]
	end = max(i[1] for i in st)

	imos = [0] * (end + 2)
	for s, t in st:
		imos[s] += 1
		imos[t + 1] -= 1
	imos_changed = [i for i in range(end + 2) if imos[i] != 0]

	result = 0
	current = 0
	for i in range(len(imos_changed)):
		current += imos[imos_changed[i]]
		if current >= 2 and i + 1 < len(imos_changed):
			result += comb(current, 2) * (imos_changed[i + 1] - imos_changed[i])

	print(result)


if __name__ == "__main__":
	main()
