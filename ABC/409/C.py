def main():
	n, l = [int(i) for i in input().split()]
	d = [int(i) for i in input().split()]

	if l % 3 != 0:
		print(0)
		exit()

	location = [0] * l
	location[0] += 1
	current_location = 0
	for i in d:
		current_location += i
		current_location %= l
		location[current_location] += 1

	result = 0
	for i in range(l // 3):
		result += location[i] * location[i + l // 3] * location[i + 2 * l // 3]

	print(result)


if __name__ == "__main__":
	main()
