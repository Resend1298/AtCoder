# TODO: review

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
				remove_end_index = trees.bisect_right(h) - 1
				if remove_end_index != -1:
					del trees[:remove_end_index + 1]
				print(len(trees))


if __name__ == "__main__":
	main()
