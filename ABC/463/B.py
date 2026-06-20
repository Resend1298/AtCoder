def main():
	n, x = input().split()
	n = int(n)
	s = [input() for _ in range(n)]

	for i in s:
		if i[ord(x) - ord('A')] == 'o':
			print("Yes")
			break
	else:
		print("No")


if __name__ == "__main__":
	main()
