# TODO: review

def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	for i in range(n):
		for j in range(i - 1, -1, -1):
			if a[j] > a[i]:
				print(j + 1)
				break
		else:
			print(-1)


if __name__ == "__main__":
	main()
