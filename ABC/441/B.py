def main():
	_ = [int(i) for i in input().split()]
	s = set(input())
	t = set(input())
	q = int(input())

	for _ in range(q):
		w = set(input())

		if w - t:
			# noinspection SpellCheckingInspection
			print("Takahashi")
		elif w - s:
			# noinspection SpellCheckingInspection
			print("Aoki")
		else:
			print("Unknown")


if __name__ == "__main__":
	main()
