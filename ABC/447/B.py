# TODO: review

from collections import Counter


def main():
	s = input()

	s_counter = Counter(s)
	most_common_count = s_counter.most_common(1)[0][1]

	s = [i for i in s if s_counter[i] != most_common_count]
	print(''.join(s))


if __name__ == "__main__":
	main()
