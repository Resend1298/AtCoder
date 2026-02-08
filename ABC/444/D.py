def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	max_a = max(a)
	imos = [0] * max_a
	for i in a:
		imos[i - 1] += 1
	for i in range(max_a - 2, -1, -1):
		imos[i] += imos[i + 1]

	result = []
	current = 0
	for i in imos:
		current += i
		result.append(str(current % 10))
		current //= 10
	if current > 0:
		result.append(str(current))

	result.reverse()
	print(''.join(result))


if __name__ == "__main__":
	main()
