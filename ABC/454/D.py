def solve():
	a = input()
	b = input()

	if a == b:
		print("Yes")
		return

	a_processed = []
	for i in a:
		a_processed.append(i)
		while len(a_processed) >= 4 and a_processed[-4:] == ['(', 'x', 'x', ')']:
			a_processed.pop()
			a_processed.pop()
			a_processed.pop()
			a_processed.pop()
			a_processed.append('x')
			a_processed.append('x')

	b_processed = []
	for i in b:
		b_processed.append(i)
		while len(b_processed) >= 4 and b_processed[-4:] == ['(', 'x', 'x', ')']:
			b_processed.pop()
			b_processed.pop()
			b_processed.pop()
			b_processed.pop()
			b_processed.append('x')
			b_processed.append('x')

	if a_processed == b_processed:
		print("Yes")
	else:
		print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
