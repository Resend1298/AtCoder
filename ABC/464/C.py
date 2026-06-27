# TODO: review

from collections import deque, Counter


def main():
	n, m = [int(i) for i in input().split()]
	adb = [[int(i) for i in input().split()] for _ in range(n)]

	color_set = set()
	color_count = Counter()

	preprocessed_adb = []
	for a, d, b in adb:
		if d == 1:
			color_set.add(b)
			color_count[b] += 1
		elif a == b:
			color_set.add(a)
			color_count[a] += 1
		else:
			preprocessed_adb.append((a, d, b))
			color_set.add(a)
			color_count[a] += 1

	preprocessed_adb.sort(key=lambda x: x[1])
	preprocessed_adb = deque(preprocessed_adb)

	for i in range(1, m + 1):
		while preprocessed_adb and preprocessed_adb[0][1] <= i:
			a, d, b = preprocessed_adb.popleft()
			color_count[a] -= 1
			if color_count[a] == 0:
				color_set.remove(a)
			color_set.add(b)
			color_count[b] += 1

		print(len(color_set))


if __name__ == "__main__":
	main()
