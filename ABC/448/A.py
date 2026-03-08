def main():
	n, x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	for i in a:
		if i < x:
			x = i
			print(1)
		else:
			print(0)


if __name__ == "__main__":
	main()
