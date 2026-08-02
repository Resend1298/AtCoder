# TODO: review

def main():
	n = int(input())
	s = input()

	result = 0
	for i in range(n):
		if s[i] == 'x' and (i == 0 or s[i - 1] == 'x') and (i == n - 1 or s[i + 1] == 'x'):
			result += 1

	print(result)


if __name__ == "__main__":
	main()
