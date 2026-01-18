# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	s = set(input())
	t = set(input())
	q = int(input())

	for _ in range(q):
		w = set(input())

		if any(i for i in w if i not in t):
			print("Takahashi")
		elif any(i for i in w if i not in s):
			print("Aoki")
		else:
			print("Unknown")


if __name__ == "__main__":
	main()
