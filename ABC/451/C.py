from sortedcontainers import SortedList


def main():
	q = int(input())

	trees = SortedList()

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, h:
				trees.add(h)
				print(len(trees))
			case 2, h:
				while trees and trees[0] <= h:
					trees.pop(0)
				print(len(trees))


if __name__ == "__main__":
	main()
