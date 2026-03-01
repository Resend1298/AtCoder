from sortedcontainers import SortedList


def main():
	s = input()

	a_index = [i for i in range(len(s)) if s[i] == 'A']
	b_index = SortedList(i for i in range(len(s)) if s[i] == 'B')
	c_index = SortedList(i for i in range(len(s)) if s[i] == 'C')
	result = 0

	for i in a_index:
		b_index_index = b_index.bisect_right(i)
		if b_index_index == len(b_index):
			break
		j = b_index[b_index_index]

		c_index_index = c_index.bisect_right(j)
		if c_index_index == len(c_index):
			break

		result += 1
		del b_index[b_index_index]
		del c_index[c_index_index]

	print(result)


if __name__ == "__main__":
	main()
