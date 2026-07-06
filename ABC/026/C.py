def main():
	n = int(input())
	children: list[list[int]] = [[] for _ in range(n)]
	for employee in range(1, n):
		b = int(input()) - 1
		children[b].append(employee)

	salary: list[int] = [1] * n

	def dfs(node: int):
		for i in children[node]:
			dfs(i)

		if children[node]:
			salary[node] = max(salary[i] for i in children[node]) + min(salary[i] for i in children[node]) + 1

	dfs(0)
	print(salary[0])


if __name__ == "__main__":
	main()
