from itertools import combinations


def main():
	s = input()

	t_index = []
	for i in range(len(s)):
		if s[i] == 't':
			t_index.append(i)

	result = 0
	for i, j in combinations(t_index, 2):
		if j - i >= 2:
			result = max(result, s[i + 1:j].count('t') / (j - i - 1))

	print(result)


if __name__ == "__main__":
	main()
