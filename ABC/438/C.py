def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	stack = []
	for i in a:
		stack.append(i)
		while len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
			stack.pop()
			stack.pop()
			stack.pop()
			stack.pop()

	print(len(stack))


if __name__ == "__main__":
	main()
