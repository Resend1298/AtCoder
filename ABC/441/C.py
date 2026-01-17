def main():
	n, k, x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.sort(reverse=True)
	a = a[n - k:]

	current = 0
	for i in range(len(a)):
		current += a[i]
		if current >= x:
			print(n - k + i + 1)
			break
	else:
		print(-1)


if __name__ == "__main__":
	main()
