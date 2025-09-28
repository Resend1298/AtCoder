def main():
	n = int(input())

	print(sum((-1) ** i * i ** 3 for i in range(1, n + 1)))


if __name__ == "__main__":
	main()
