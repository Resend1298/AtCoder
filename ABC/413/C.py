from collections import deque


def main():
	q = int(input())

	a = deque()

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				a.append([query[2], query[1]])
			case 2:
				result = 0

				while query[1] > 0:
					if a[0][1] <= query[1]:
						result += a[0][0] * a[0][1]
						query[1] -= a[0][1]
						a.popleft()
					else:
						result += a[0][0] * query[1]
						a[0][1] -= query[1]
						query[1] = 0

				print(result)


if __name__ == "__main__":
	main()
