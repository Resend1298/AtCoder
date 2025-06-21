def main():
	n, q = [int(i) for i in input().split()]

	current = [[] for _ in range(n + 1)]
	cow = set()

	for _ in range(q):
		query = input().split()
		query[0] = int(query[0])
		query[1] = int(query[1])

		match query[0]:
			case 1:
				current[query[1]] = current[0]
				cow.add(id(current[0]))
			case 2:
				if id(current[query[1]]) in cow:
					current[query[1]] = current[query[1]].copy()

				current[query[1]].append(query[2])
			case 3:
				current[0] = current[query[1]]
				cow.add(id(current[query[1]]))

	print(''.join(current[0]))


if __name__ == "__main__":
	main()
