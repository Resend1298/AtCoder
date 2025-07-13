# TODO: review

def main():
	n, l, r = [int(i) for i in input().split()]
	result = 0
	for _ in range(n):
		x, y = [int(i) for i in input().split()]
		if x <= l and y >= r:
			result += 1
	print(result)


if __name__ == "__main__":
	main()
