def main():
	n, t = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.append(t)
	result = 0
	pre_open_time = 0

	for i in a:
		if pre_open_time < i:
			result += i - pre_open_time
			pre_open_time = i + 100

	print(result)


if __name__ == "__main__":
	main()
