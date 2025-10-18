from collections import Counter


def main():
	n, k = [int(i) for i in input().split()]
	s = input()

	substr = []
	for i in range(n - k + 1):
		substr.append(s[i:i + k])

	substr_counter = Counter(substr)
	print(substr_counter.most_common(1)[0][1])
	most_common_substr = [i[0] for i in substr_counter.most_common() if i[1] == substr_counter.most_common(1)[0][1]]
	most_common_substr.sort()
	print(*most_common_substr)


if __name__ == "__main__":
	main()
