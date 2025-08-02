def main():
	_, _ = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	for i in b:
		if i in a:
			a.remove(i)

	print(*a)


if __name__ == "__main__":
	main()
