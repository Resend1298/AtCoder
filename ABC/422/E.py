# CPython TLE, PyPy AC

from random import sample


def main():
	n = int(input())
	points = [[int(i) for i in input().split()] for _ in range(n)]

	for _ in range(100):
		point_a, point_b = sample(points, 2)
		x1, y1 = point_a
		x2, y2 = point_b

		a = y1 - y2
		b = x2 - x1
		c = x1 * y2 - x2 * y1

		count = 0
		for x, y in points:
			if a * x + b * y + c == 0:
				count += 1
		if count > n / 2:
			print("Yes")
			print(a, b, c)
			exit()

	print("No")


if __name__ == "__main__":
	main()
