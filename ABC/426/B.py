from collections import Counter


def main():
	s = input()

	s_count = Counter(s)

	print(s_count.most_common()[1][0])


if __name__ == "__main__":
	main()
