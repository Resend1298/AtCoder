# TODO: review

def main():
	q = int(input())

	a = []
	head = 0
	tail = 0

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				a.append([tail, tail + query[1] - 1, query[2]])
				tail += query[1]
			case 2:
				result = 0
				while query[1] > 0 and query[1] >= a[head][1] - a[head][0] + 1:
					result += a[head][2] * (a[head][1] - a[head][0] + 1)
					query[1] -= a[head][1] - a[head][0] + 1
					head += 1
				if query[1] > 0:
					result += a[head][2] * query[1]
					a[head][0] += query[1]
				print(result)


if __name__ == "__main__":
	main()
