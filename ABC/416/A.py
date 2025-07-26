def main():
	n, l, r = [int(i) for i in input().split()]
	s = input()

	print("Yes" if all(i == 'o' for i in s[l - 1:r]) else "No")


if __name__ == "__main__":
	main()
