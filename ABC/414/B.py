def main():
	n = int(input())
	c = []
	l = []
	for _ in range(n):
		cl = input().split()
		c.append(cl[0])
		l.append(int(cl[1]))

	if sum(l) > 100:
		print("Too Long")
		exit()

	result = []
	for i in range(n):
		result.append(c[i] * l[i])
	print(''.join(result))


if __name__ == "__main__":
	main()
