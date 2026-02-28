from sortedcontainers import SortedList


def main():
	s = input()

	a_index = [i for i in range(len(s)) if s[i] == 'A']
	b_index = SortedList([i for i in range(len(s)) if s[i] == 'B'])
	c_index = SortedList([i for i in range(len(s)) if s[i] == 'C'])
	result = 0

	for a in a_index:
		b = b_index.bisect_right(a)
		if b == len(b_index):
			break
		c = c_index.bisect_right(b_index[b])
		if c == len(c_index):
			break

		result += 1
		del b_index[b]
		del c_index[c]

	print(result)


if __name__ == "__main__":
	main()
