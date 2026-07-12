def solve():
	s = input()

	stack = []
	for i in s[::-1]:
		stack.append(i)
		if i == 'A':
			if len(stack) >= 3 and stack[-3:] == ['C', 'B', 'A']:
				stack.pop()
				stack.pop()
				stack.pop()
			elif len(stack) >= 2 and stack[-2:] == ['B', 'A']:
				stack.pop()
				stack.pop()
			else:
				stack.pop()

	print(len(stack))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
