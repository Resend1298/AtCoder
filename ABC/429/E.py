from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)
	safe = set()
	danger = set()
	s = input()
	for i in range(n):
		if s[i] == 'S':
			safe.add(i)
		else:
			danger.add(i)
	danger_list = list(danger)

	for i in danger_list:
		q = deque()
		visited = [False] * n

		q.append((i, 0))
		visited[i] = True

		result = []

		while len(result) < 2 and q:
			tmp, cost = q.popleft()

			if tmp in safe:
				result.append(cost)

			for j in edges[tmp]:
				if not visited[j]:
					q.append((j, cost + 1))
					visited[j] = True

		print(result[0] + result[1])


if __name__ == "__main__":
	main()
