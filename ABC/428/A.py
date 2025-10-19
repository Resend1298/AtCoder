# TODO: review

def main():
	s, a, b, x = [int(i) for i in input().split()]

	print(x // (a + b) * s * a + min(a, x % (a + b)) * s)


if __name__ == "__main__":
	main()
