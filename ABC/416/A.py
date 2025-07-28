def main():
	n, l, r = [int(i) for i in input().split()]
	l -= 1
	r -= 1
	s = input()

	print("Yes" if all(s[i] == 'o' for i in range(l, r + 1)) else "No")


if __name__ == "__main__":
	main()
