# TODO: review

def main():
	n = int(input())

	visited = set()

	while n not in visited:
		visited.add(n)

		n = str(n)
		tmp = 0
		for i in n:
			current = int(i)
			tmp += current ** 2
		n = tmp

	if n == 1:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
