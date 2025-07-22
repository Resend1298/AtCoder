def solve():
	n = int(input())
	s = [int(i) for i in list(input())]

	# "all chemicals are mixed" is dangerous
	# or
	# no chemical can be poured first
	if s[-1] == 1 or all(s[2 ** i - 1] == 1 for i in range(n)):
		print("No")
		return

	visited = [False] * n
	visited_status = set()
	result = False

	def dfs(i, status):
		nonlocal result

		visited[i] = True
		status += 2 ** i

		if status == 2 ** n - 1:
			result = True
			return
		if status in visited_status:
			visited[i] = False
			return
		visited_status.add(status)

		for j in range(n):
			if not visited[j] and s[status + 2 ** j - 1] == 0:
				dfs(j, status)

		visited[i] = False

	for i in range(n):
		if s[2 ** i - 1] == 0:
			dfs(i, 0)

	print("Yes" if result else "No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
