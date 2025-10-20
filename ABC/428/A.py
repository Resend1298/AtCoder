def main():
	s, a, b, x = [int(i) for i in input().split()]

	print(x // (a + b) * s * a + min(x % (a + b), a) * s)


if __name__ == "__main__":
	main()
