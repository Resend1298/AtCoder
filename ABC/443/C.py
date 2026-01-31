def main():
	n, t = [int(i) for i in input().split()]

	if n == 0:
		print(t)
		exit()

	a = [int(i) for i in input().split()]

	pre_open_time = 0
	result = 0

	for i in a:
		if i > pre_open_time:
			result += i - pre_open_time
			pre_open_time = i + 100

	if t > pre_open_time:
		result += t - pre_open_time

	print(result)


if __name__ == "__main__":
	main()
