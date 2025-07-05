def main():
	n = int(input())
	s = list(set([input() for _ in range(n)]))

	new = set()
	for i in range(len(s)):
		for j in range(len(s)):
			if i != j:
				new.add(s[i] + s[j])

	print(len(new))


if __name__ == "__main__":
	main()
