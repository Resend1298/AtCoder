def main():
	n = int(input())
	s = input()

	a_index = []
	b_index = []
	for i in range(n * 2):
		if s[i] == 'A':
			a_index.append(i)
		else:
			b_index.append(i)

	result_a = 0
	for i in range(n):
		result_a += abs(a_index[i] - 2 * i)

	result_b = 0
	for i in range(n):
		result_b += abs(b_index[i] - 2 * i)

	print(min(result_a, result_b))


if __name__ == "__main__":
	main()
