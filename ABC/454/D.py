def remove_parentheses(s):
	result = []
	for i in s:
		result.append(i)
		while len(result) >= 4 and result[-4:] == ['(', 'x', 'x', ')']:
			result[-4:] = ['x', 'x']
	return ''.join(result)


def solve():
	a = input()
	b = input()

	if remove_parentheses(a) == remove_parentheses(b):
		print("Yes")
	else:
		print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
