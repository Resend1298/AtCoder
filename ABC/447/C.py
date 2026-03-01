from collections import deque


def main():
	s = input()
	t = input()

	if s.replace('A', '') != t.replace('A', ''):
		print(-1)
		exit()

	s = deque(s)
	t = deque(t)
	result = 0

	while s and t:
		if s[0] == t[0]:
			s.popleft()
			t.popleft()
		elif s[0] == 'A':
			s.popleft()
			result += 1
		else:
			t.popleft()
			result += 1

	result += len(s) + len(t)
	print(result)


if __name__ == "__main__":
	main()
