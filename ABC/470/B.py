from collections import Counter


def main():
	n = int(input())
	c = [int(i) for i in input().split()]

	c_counter = Counter(c)
	print(n - c_counter.most_common(1)[0][1])


if __name__ == "__main__":
	main()
