def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	if a == b:
		print("Yes")
		exit()

	status = 0
	taking = 0
	for i in range(n):
		if status == 0 or status == 2:
			if a[i] == b[i]:
				continue
		elif status == 1:
			if i + 1 < n and a[i + 1] == b[i]:
				continue
			if i + 1 == n and b[i] == taking:
				continue

		match status:
			case 0:
				if i + 1 < n and b[i] == a[i + 1]:
					taking = a[i]
					status = 1
				else:
					break

			case 1:
				if b[i] == taking:
					status = 2
				else:
					break

			case 2:
				break
	else:
		print("Yes")
		exit()

	a.reverse()
	b.reverse()

	status = 0
	taking = 0
	for i in range(n):
		if status == 0 or status == 2:
			if a[i] == b[i]:
				continue
		elif status == 1:
			if i + 1 < n and a[i + 1] == b[i]:
				continue
			if i + 1 == n and b[i] == taking:
				continue

		match status:
			case 0:
				if i + 1 < n and b[i] == a[i + 1]:
					taking = a[i]
					status = 1
				else:
					break

			case 1:
				if b[i] == taking:
					status = 2
				else:
					break

			case 2:
				break
	else:
		print("Yes")
		exit()

	print("No")


if __name__ == "__main__":
	main()
