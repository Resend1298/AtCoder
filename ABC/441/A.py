def main():
	p, q = [int(i) for i in input().split()]
	x, y = [int(i) for i in input().split()]

	if p <= x < p + 100 and q <= y < q + 100:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
