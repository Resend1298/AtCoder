# TODO: review

def solve():
	n, m, k = [int(i) for i in input().split()]
	s = input()
	edges = [[] for _ in range(n)]
	edges_to = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges_to[v].append(u)

	target = set([i for i in range(n) if s[i] == 'A'])
	all_set = set([i for i in range(n)])

	for i in range(k, 0, -1):
		target = all_set - target
		new_target = set()
		while target:
			tmp = target.pop()
			for j in edges_to[tmp]:
				new_target.add(j)
		target = all_set - new_target
		new_target = set()
		while target:
			tmp = target.pop()
			for j in edges_to[tmp]:
				new_target.add(j)
		target = new_target

	if 0 in target:
		print("Alice")
	else:
		print("Bob")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
