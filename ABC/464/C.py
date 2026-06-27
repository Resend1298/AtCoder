from collections import Counter, deque


def main():
	n, m = [int(i) for i in input().split()]
	adb = [[int(i) for i in input().split()] for _ in range(n)]

	color_set = set()
	color_counter = Counter()

	adb_preprocessed = []
	for a, d, b in adb:
		if d == 1 or a == b:
			color_set.add(b)
			color_counter[b] += 1
		else:
			color_set.add(a)
			color_counter[a] += 1
			adb_preprocessed.append((a, d, b))
	adb_preprocessed = deque(sorted(adb_preprocessed, key=lambda x: x[1]))

	for i in range(1, m + 1):
		while adb_preprocessed and adb_preprocessed[0][1] <= i:
			a, d, b = adb_preprocessed.popleft()
			color_counter[a] -= 1
			if color_counter[a] == 0:
				color_set.remove(a)
			color_set.add(b)
			color_counter[b] += 1

		print(len(color_set))


if __name__ == "__main__":
	main()
