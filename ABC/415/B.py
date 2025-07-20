# TODO: review

from collections import deque


def main():
	s = input()

	location = deque()
	for i in range(len(s)):
		if s[i] == '#':
			location.append(i)

	while location:
		print(f"{location.popleft() + 1},{location.popleft() + 1}")


if __name__ == "__main__":
	main()
