def main():
	k = int(input())
	a = [int(i) for i in input().split()]

	if 9 not in a:
		print(-1)
	else:
		print(min(a))


if __name__ == "__main__":
	main()
