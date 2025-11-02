# TODO: review

from sortedcontainers import SortedList


def main():
	n, a, b = [int(i) for i in input().split()]
	s = input()

	b_index = SortedList()
	last_b_index = -1
	for i in range(n):
		if s[i] == 'b':
			b_index.add(i)
			if last_b_index == -1:
				last_b_index = i
	if last_b_index != -1:
		last_b_index = -2

	r = 0
	result = 0
	current_a = 0
	current_b = 0
	if s[0] == 'a':
		current_a += 1
	else:
		current_b += 1
		last_b_index = 0

	for l in range(n):
		while r + 1 < n and current_a < a:
			r += 1
			if s[r] == 'a':
				current_a += 1
			else:
				current_b += 1
				last_b_index = r
		if r == n - 1 and current_a < a:
			break

		if current_b < b:
			if last_b_index != -1 and last_b_index != -2:
				tmp = b_index.bisect_left(last_b_index)
				tmp2 = min(len(b_index) - 1, tmp + b - current_b)
				tmp2 = b_index[tmp2]
				if tmp2 < r or tmp + b - current_b >= len(b_index):
					result += n - r
				else:
					result += tmp2 - r
			elif last_b_index == -1:
				result += n - r
			else:
				tmp = b - 1
				if tmp >= len(b_index):
					result += n - r
				else:
					tmp2 = b_index[tmp]
					result += tmp2 - r

		if s[l] == 'a':
			current_a -= 1
		else:
			current_b -= 1

		if l == r and r + 1 < n:
			r += 1
			if s[r] == 'a':
				current_a += 1
			else:
				current_b += 1
				last_b_index = r

	print(result)


if __name__ == "__main__":
	main()
