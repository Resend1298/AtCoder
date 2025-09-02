from collections import deque


def main():
	ax, ay, bx, by = [int(i) for i in input().split()]
	n, m, l = [int(i) for i in input().split()]
	move_a = deque([[i[0], int(i[1])] for i in [input().split() for _ in range(m)]])
	move_b = deque([[i[0], int(i[1])] for i in [input().split() for _ in range(l)]])

	result = 0

	while move_a or move_b:
		min_move = min(move_a[0][1], move_b[0][1])

		match (move_a[0][0], move_b[0][0]):
			# for the same direction cases, they will only meet when they start at the same point
			case ('U', 'U'):
				if ax == bx and ay == by:
					result += min_move
				ax -= min_move
				bx -= min_move
			case ('D', 'D'):
				if ax == bx and ay == by:
					result += min_move
				ax += min_move
				bx += min_move
			case ('L', 'L'):
				if ax == bx and ay == by:
					result += min_move
				ay -= min_move
				by -= min_move
			case ('R', 'R'):
				if ax == bx and ay == by:
					result += min_move
				ay += min_move
				by += min_move

			# for the opposite direction cases, they will only meet when:
			# 1. they are on the same line
			# 2. they are moving towards each other (and can't be at the same point at the start)
			# 3. the distance between them is less enough to meet within the min_move steps
			# 4. the middle point has to be an integer point
			case ('U', 'D'):
				if ay == by and ax > bx and (ax - bx) <= 2 * min_move and (ax - bx) % 2 == 0:
					result += 1
				ax -= min_move
				bx += min_move
			case ('D', 'U'):
				if ay == by and ax < bx and (bx - ax) <= 2 * min_move and (bx - ax) % 2 == 0:
					result += 1
				ax += min_move
				bx -= min_move
			case ('L', 'R'):
				if ax == bx and ay > by and (ay - by) <= 2 * min_move and (ay - by) % 2 == 0:
					result += 1
				ay -= min_move
				by += min_move
			case ('R', 'L'):
				if ax == bx and ay < by and (by - ay) <= 2 * min_move and (by - ay) % 2 == 0:
					result += 1
				ay += min_move
				by -= min_move

			# for the cross direction cases, they will only meet when:
			# 1. the two paths cross each other (the cross point can't be at the start but can be at the end)
			# 2. they will reach the cross point at the same time
			case ('U', 'L'):
				if ax > bx >= ax - min_move and by > ay >= by - min_move and (ax - bx) == (by - ay):
					result += 1
				ax -= min_move
				by -= min_move
			case ('U', 'R'):
				if ax > bx >= ax - min_move and by < ay <= by + min_move and (ax - bx) == (ay - by):
					result += 1
				ax -= min_move
				by += min_move
			case ('D', 'L'):
				if ax < bx <= ax + min_move and by > ay >= by - min_move and (bx - ax) == (by - ay):
					result += 1
				ax += min_move
				by -= min_move
			case ('D', 'R'):
				if ax < bx <= ax + min_move and by < ay <= by + min_move and (bx - ax) == (ay - by):
					result += 1
				ax += min_move
				by += min_move
			case ('L', 'U'):
				if ay > by >= ay - min_move and bx > ax >= bx - min_move and (ay - by) == (bx - ax):
					result += 1
				ay -= min_move
				bx -= min_move
			case ('L', 'D'):
				if ay > by >= ay - min_move and bx < ax <= bx + min_move and (ay - by) == (ax - bx):
					result += 1
				ay -= min_move
				bx += min_move
			case ('R', 'U'):
				if ay < by <= ay + min_move and bx > ax >= bx - min_move and (by - ay) == (bx - ax):
					result += 1
				ay += min_move
				bx -= min_move
			case ('R', 'D'):
				if ay < by <= ay + min_move and bx < ax <= bx + min_move and (by - ay) == (ax - bx):
					result += 1
				ay += min_move
				bx += min_move

		move_a[0][1] -= min_move
		move_b[0][1] -= min_move
		if move_a[0][1] == 0:
			move_a.popleft()
		if move_b[0][1] == 0:
			move_b.popleft()

	print(result)


if __name__ == "__main__":
	main()
