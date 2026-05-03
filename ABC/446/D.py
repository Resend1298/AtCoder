def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	max_len = {}

	for i in a:
		if i - 1 not in max_len:
			max_len[i] = 1
		else:
			max_len[i] = max_len[i - 1] + 1

	print(max(max_len.values()))


if __name__ == "__main__":
	main()
