# TODO: review

def main():
	n = int(input())

	result = 0
	r = 2

	for l in range(1, n):
		if not r > l:
			r = l + 1
		while r <= n:
			print(f"? {l} {r}")
			if input() == "Yes":
				r += 1
			else:
				break
		result += r - l - 1

	print(f"! {result}")


if __name__ == "__main__":
	main()
