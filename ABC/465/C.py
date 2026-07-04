def main():
	n = int(input())
	s = input()

	result = [-1] * n
	left = 0
	right = n - 1
	current_right = True
	for i in range(n, 0, -1):
		if s[i - 1] == 'o':
			current_right = not current_right
		if current_right:
			result[right] = i
			right -= 1
		else:
			result[left] = i
			left += 1

	print(*result)


if __name__ == "__main__":
	main()
