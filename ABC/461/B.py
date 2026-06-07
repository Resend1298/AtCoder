# TODO: review

def main():
	n = int(input())
	a = [int(i) - 1 for i in input().split()]
	b = [int(i) - 1 for i in input().split()]

	for i in range(n):
		if b[a[i]] != i:
			print("No")
			break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
