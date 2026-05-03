def solve():
	n, m, k = [int(i) for i in input().split()]
	s = input()
	edges_rev = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges_rev[v].append(u)

	b_target = set(i for i in range(n) if s[i] == 'B')
	all_set = set(range(n))

	for _ in range(k, 0, -1):
		b_target = set(j for i in b_target for j in edges_rev[i])
		a_target = all_set - b_target
		a_target: set[int] = set(j for i in a_target for j in edges_rev[i])
		b_target = all_set - a_target

	# noinspection PyUnboundLocalVariable
	print("Alice" if 0 in a_target else "Bob")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
