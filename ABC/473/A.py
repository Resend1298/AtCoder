# TODO: review

def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	print(sum(a[n // 2:]))


if __name__ == "__main__":
	main()
