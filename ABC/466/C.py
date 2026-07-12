def main():
	n = int(input())

	result = 0
	r = 1

	for l in range(n - 1):
		if not l < r:
			r = l + 1

		while r < n and input(f"? {l + 1} {r + 1}\n") == "Yes":
			r += 1

		result += r - l - 1

	print(f"! {result}")


if __name__ == "__main__":
	main()
