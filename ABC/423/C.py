def left_first(leftest_unlocked, rightest_unlocked, r, l):
	result = 0

	for i in range(r - 1, leftest_unlocked, -1):
		if l[i] == 1:
			result += 1
			l[i] = 0

	result += 1

	for i in range(leftest_unlocked + 1, rightest_unlocked):
		if l[i] == 0:
			result += 1
		else:
			result += 2

	result += 1

	return result


def right_first(leftest_unlocked, rightest_unlocked, r, l):
	result = 0

	for i in range(r, rightest_unlocked):
		if l[i] == 1:
			result += 1
			l[i] = 0

	result += 1

	for i in range(rightest_unlocked - 1, leftest_unlocked, -1):
		if l[i] == 0:
			result += 1
		else:
			result += 2

	result += 1

	return result


def main():
	n, r = [int(i) for i in input().split()]
	l = [int(i) for i in input().split()]

	for i in range(r):
		if l[i] == 0:
			leftest_unlocked = i
			break
	else:
		leftest_unlocked = None
	for i in range(n - 1, r - 1, -1):
		if l[i] == 0:
			rightest_unlocked = i
			break
	else:
		rightest_unlocked = None

	if leftest_unlocked is None and rightest_unlocked is None:
		print(0)
	elif leftest_unlocked is None:
		result = 0
		for i in range(r, rightest_unlocked):
			if l[i] == 0:
				result += 1
			else:
				result += 2
		result += 1
		print(result)
	elif rightest_unlocked is None:
		result = 0
		for i in range(r - 1, leftest_unlocked, -1):
			if l[i] == 0:
				result += 1
			else:
				result += 2
		result += 1
		print(result)
	else:
		print(min(left_first(leftest_unlocked, rightest_unlocked, r, l.copy()),
		          right_first(leftest_unlocked, rightest_unlocked, r, l.copy())))


if __name__ == "__main__":
	main()
