def main():
	t = int(input())

	for _ in range(t):
		n = int(input())
		a = [int(i) for i in input().split()]

		if n == 2:
			print("Yes")
			continue

		# r == -1
		tmp = list(set(a))
		if len(tmp) == 2 and tmp[0] == -tmp[1] and abs(a.count(tmp[0]) - a.count(tmp[1])) <= 1:
			print("Yes")
			continue

		# r != -1
		a.sort(key=lambda x: abs(x))
		for i in range(1, n - 1):
			if a[i] ** 2 != a[i - 1] * a[i + 1]:
				print("No")
				break
		else:
			print("Yes")


if __name__ == "__main__":
	main()
