# TODO: TLE

from collections import Counter


def main():
	n = int(input())
	imos = [[Counter() for _ in range(2000)] for _ in range(2000)]
	for i in range(n):
		u, d, l, r = [int(i) - 1 for i in input().split()]
		imos[u][l].update({i: 1})
		if d + 1 < 2000 and r + 1 < 2000:
			imos[d + 1][r + 1].update({i: 1})
		if r + 1 < 2000:
			imos[u][r + 1].update({i: -1})
		if d + 1 < 2000:
			imos[d + 1][l].update({i: -1})

	for i in range(2000):
		for j in range(1, 2000):
			imos[i][j].update(imos[i][j - 1])
			for key in list(imos[i][j].keys()):
				if imos[i][j][key] == 0:
					del imos[i][j][key]

	for i in range(2000):
		for j in range(1, 2000):
			imos[j][i].update(imos[j - 1][i])
			for key in list(imos[j][i].keys()):
				if imos[j][i][key] == 0:
					del imos[j][i][key]

	imos_count = [0] * n
	empty_count = 0
	for i in range(2000):
		for j in range(2000):
			if len(imos[i][j]) == 1:
				imos_count[list(imos[i][j].keys())[0]] += 1
			elif len(imos[i][j]) == 0:
				empty_count += 1

	for i in imos_count:
		print(empty_count + i)


if __name__ == "__main__":
	main()
