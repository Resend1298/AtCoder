# TODO: review

def main():
	t = int(input())
	for _ in range(t):
		n = int(input())
		s = [int(i) for i in list(input())]

		visited = [False] * n
		visited_status = set()
		result = False

		def dfs(i, status):
			if status in visited_status:
				return
			visited_status.add(status)

			nonlocal result

			visited[i] = True

			if status == 2 ** n - 1 and s[status - 1] == 0:
				result = True
				return

			for j in range(n):
				if not visited[j] and s[status + 2 ** j - 1] == 0:
					dfs(j, status + 2 ** j)
				if result:
					return

			visited[i] = False

		for i in range(n):
			if result:
				break
			if s[2 ** i - 1] == 0:
				dfs(i, 2 ** i)

		print("Yes" if result else "No")


if __name__ == "__main__":
	main()
