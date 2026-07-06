def main():
	n, x = input().split()
	n = int(n)
	s = [input() for _ in range(n)]

	x = ord(x) - ord('A')

	for i in s:
		if i[x] == 'o':
			print("Yes")
			break
	else:
		print("No")


if __name__ == "__main__":
	main()
