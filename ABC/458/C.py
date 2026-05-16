def main():
	s = input()

	s_len = len(s)
	c_index = [i for i in range(s_len) if s[i] == 'C']
	result = 0

	for i in c_index:
		l = i
		r = s_len - i - 1
		result += min(l, r) + 1

	print(result)


if __name__ == "__main__":
	main()
