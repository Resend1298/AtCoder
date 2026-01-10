def main():
	n = int(input())
	t = [int(i) for i in input().split()]

	result = sorted(enumerate(t), key=lambda x: x[1])

	print(*(i[0] + 1 for i in result[:3]))


if __name__ == "__main__":
	main()
