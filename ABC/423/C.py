# TODO: review

def main():
	n, r = [int(i) for i in input().split()]
	l = [int(i) for i in input().split()]

	if all(i == 1 for i in l):
		print(0)
		exit()

	l_copy = l.copy()

	for i in range(r):
		if l[i] == 0:
			left = i
			break
	else:
		left = -1
	for i in range(n - 1, r - 1, -1):
		if l[i] == 0:
			right = i
			break
	else:
		right = -1

	if left == -1:
		result = 0
		for i in range(r, right):
			if l[i] == 0:
				result += 1
			else:
				result += 2
		result += 1
		print(result)
		exit()
	elif right == -1:
		result = 0
		for i in range(r - 1, left, -1):
			if l[i] == 0:
				result += 1
			else:
				result += 2
		result += 1
		print(result)
		exit()

	result_left = 0
	for i in range(r - 1, left, -1):
		if l[i] == 1:
			result_left += 1
			l[i] = 0
	result_left += 1
	for i in range(left + 1, right):
		if l[i] == 0:
			result_left += 1
		else:
			result_left += 2
	result_left += 1

	result_right = 0
	l = l_copy
	for i in range(r, right):
		if l[i] == 1:
			result_right += 1
			l[i] = 0
	result_right += 1
	for i in range(right - 1, left, -1):
		if l[i] == 0:
			result_right += 1
		else:
			result_right += 2
	result_right += 1

	print(min(result_left, result_right))


if __name__ == "__main__":
	main()
