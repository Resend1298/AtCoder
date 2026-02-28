from collections import deque


def main():
	s = input()
	t = input()

	result = 0
	s = deque(s)
	t = deque(t)

	while s and t:
		if s[0] == t[0]:
			s.popleft()
			t.popleft()
			continue

		if s[0] != 'A' and t[0] != 'A':
			print(-1)
			exit()

		if s[0] == 'A':
			s.popleft()
			result += 1
		else:
			t.popleft()
			result += 1

	if not s and not t:
		print(result)
	elif not s and all(i == 'A' for i in t):
		print(result + len(t))
	elif not t and all(i == 'A' for i in s):
		print(result + len(s))
	else:
		print(-1)


if __name__ == "__main__":
	main()
