def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	for i in range(n):
		if l[i] == 1:
			left = i
			break
	else:
		left = n

	for i in range(n - 1, -1, -1):
		if l[i] == 1:
			right = i + 1
			break
	else:
		right = 0

	if right - left <= 1:
		print(0)
	else:
		print(right - left - 1)


if __name__ == "__main__":
	main()
