def main():
	n, a, b = [int(i) for i in input().split()]
	s = input()

	print(s[a:n - b])


if __name__ == "__main__":
	main()
