# TODO: review

from collections import Counter


def main():
	n = int(input())
	s = [input().lower() for _ in range(n)]

	s_counter = Counter(s)
	print(s_counter.most_common(1)[0][1])


if __name__ == "__main__":
	main()
