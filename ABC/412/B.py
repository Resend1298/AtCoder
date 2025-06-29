# TODO: review

def main():
	s = input()
	t = set(input())

	for i in range(1, len(s)):
		if 'A' <= s[i] <= 'Z' and s[i - 1] not in t:
			print("No")
			break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
