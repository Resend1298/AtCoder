# TODO: review

def main():
	n = int(input())
	xy = [[int(i) for i in input().split()] for _ in range(n)]

	xy.sort(key=lambda x: x[0])
	result = 0
	pre_min = float("inf")

	for x, y in xy:
		if y < pre_min:
			result += 1
			pre_min = y

	print(result)


if __name__ == "__main__":
	main()
