def main():
	n, m = [int(i) for i in input().split()]
	f = [int(i) - 1 for i in input().split()]

	tmp = set()
	for i in f:
		tmp.add(i)
	if len(tmp) == n:
		print("Yes")
	else:
		print("No")

	for i in range(m):
		if i not in tmp:
			print("No")
			break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
