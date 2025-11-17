# TODO: review

def main():
	numbers = [int(i) for i in input().split()]

	numbers.sort(reverse=True)
	print(numbers[0] * 100 + numbers[1] * 10 + numbers[2])


if __name__ == "__main__":
	main()
