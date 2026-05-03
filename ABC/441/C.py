def main():
	n, k, x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.sort(reverse=True)
	current = 0

	for i in range(n - k, n):
		current += a[i]
		if current >= x:
			print(i + 1)
			break
	else:
		print(-1)


if __name__ == "__main__":
	main()
