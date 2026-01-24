# TODO: unsolved

from collections import defaultdict


def main():
	n, q = [int(i) for i in input().split()]

	location = []
	a = []

	for _ in range(n):
		x, y = [int(i) for i in input().split()]

		if x > 0 and y > 0:
			location.append((1, -y / x))
			a.append((1, -y / x))
		elif x < 0 < y:
			location.append((7, -y / x))
			a.append((7, -y / x))
		elif x < 0 and y < 0:
			location.append((5, -y / x))
			a.append((5, -y / x))
		elif x > 0 > y:
			location.append((3, -y / x))
			a.append((3, -y / x))
		elif y == 0 and x > 0:
			location.append((2, 0))
			a.append((2, 0))
		elif y == 0 and x < 0:
			location.append((6, 0))
			a.append((6, 0))
		elif x == 0 and y > 0:
			location.append((0, 0))
			a.append((0, 0))
		elif x == 0 and y < 0:
			location.append((4, 0))
			a.append((4, 0))

	location.sort()
	start_index = defaultdict(lambda: float("inf"))
	end_index = defaultdict(lambda: float("-inf"))
	for i in range(n):
		start_index[location[i]] = min(start_index[location[i]], i)
		end_index[location[i]] = max(end_index[location[i]], i)

	for _ in range(q):
		x, y = [int(i) for i in input().split()]
		x = a[x - 1]
		y = a[y - 1]
		if x[0] < y[0] or (x[0] == y[0] and x[1] <= y[1]):
			x_index = start_index[x]
			y_index = end_index[y]
			print(y_index - x_index + 1)
		else:
			x_index = start_index[x]
			y_index = end_index[y]
			print(n - x_index + y_index + 1)


if __name__ == "__main__":
	main()
