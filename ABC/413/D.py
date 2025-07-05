def main():
	t = int(input())

	for _ in range(t):
		n = int(input())
		a = [int(i) for i in input().split()]

		if n == 2:
			print("Yes")
			continue

		if n == 3:
			a.sort()
			if a[1] ** 2 == a[0] * a[2]:
				print("Yes")
				continue
			a.sort(key=lambda x: abs(x))
			if a[1] ** 2 == a[0] * a[2]:
				print("Yes")
				continue

			tmp = list(set(a))
			if len(tmp) == 2 and tmp[0] == -tmp[1]:
				print("Yes")
				continue

			print("No")
			continue

		tmp = list(set(a))
		if len(tmp) == 2 and tmp[0] == -tmp[1] and abs(a.count(tmp[0]) - a.count(tmp[1])) <= 1:
			print("Yes")
			continue

		a.sort()
		for i in range(2, n):
			if a[i - 1] ** 2 != a[i - 2] * a[i]:
				break
		else:
			print("Yes")
			continue
		a.sort(key=lambda x: abs(x))
		for i in range(2, n):
			if a[i - 1] ** 2 != a[i - 2] * a[i]:
				print("No")
				break
		else:
			print("Yes")
			continue


if __name__ == "__main__":
	main()
