# TODO: review

def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	left = float("inf")
	right = -1
	for i in range(n):
		if l[i] == 1:
			left = i
			break
	for i in range(n - 1, -1, -1):
		if l[i] == 1:
			right = i
			break

	if left >= right:
		print(0)
	else:
		print(right - left)


if __name__ == "__main__":
	main()
