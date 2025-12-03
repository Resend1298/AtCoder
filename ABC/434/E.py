from collections import defaultdict

from sortedcontainers import SortedKeyList


def main():
	n = int(input())
	rabbits = [[int(i) for i in input().split()] for _ in range(n)]

	jump_coordinates = defaultdict(set)
	for i in range(n):
		x, r = rabbits[i]
		jump_coordinates[x - r].add(i)
		jump_coordinates[x + r].add(i)

	q = SortedKeyList(key=lambda i: i[1])
	for k, v in jump_coordinates.items():
		q.add((k, len(v)))

	result = 0
	processed_coordinates = set()
	while q:
		coordinate, _ = q.pop(0)

		if coordinate in processed_coordinates:
			continue
		processed_coordinates.add(coordinate)

		if jump_coordinates[coordinate]:
			result += 1
			rabbit = jump_coordinates[coordinate].pop()
			x, r = rabbits[rabbit]
			other_coordinate = x + r if coordinate == x - r else x - r
			jump_coordinates[other_coordinate].remove(rabbit)
			q.add((other_coordinate, len(jump_coordinates[other_coordinate])))

	print(result)


if __name__ == "__main__":
	main()
