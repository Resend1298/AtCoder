def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	sum_a = sum(a)
	for i in a:
		if sum_a - i == m:
			print("Yes")
			break
	else:
		print("No")


if __name__ == "__main__":
	main()
