def main():
	w, b = [int(i) for i in input().split()]

	w *= 1000
	result = 0
	while b * result <= w:
		result += 1

	print(result)


if __name__ == "__main__":
	main()
