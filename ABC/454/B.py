def main():
	n, m = [int(i) for i in input().split()]
	f = [int(i) - 1 for i in input().split()]

	f_set = set(f)

	if len(f_set) == n:
		print("Yes")
	else:
		print("No")

	if all(i in f_set for i in range(m)):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
