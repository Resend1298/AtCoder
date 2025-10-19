# TODO: TLE

def main():
	q = int(input())

	stack = []
	stack_history = {0: []}
	stack_size = 0

	for _ in range(q):
		match input().split():
			case ['1', c]:
				stack.append(c)
				stack_size += 1

				while len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
					stack.pop()
					stack.pop()
				stack_history[stack_size] = stack.copy()
				if stack:
					print("No")
				else:
					print("Yes")
			case ['2']:
				stack = stack_history[stack_size - 1].copy()
				stack_size -= 1
				if stack:
					print("No")
				else:
					print("Yes")


if __name__ == "__main__":
	main()
