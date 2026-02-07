def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_max = max(a)
	imos = [0] * a_max
	for i in a:
		imos[i - 1] += 1
	imos.reverse()

	imos_sum = [imos[0]]
	for i in range(1, a_max):
		imos_sum.append(imos_sum[-1] + imos[i])

	current = 0
	result = []
	for i in range(a_max - 1, -1, -1):
		current += imos_sum[i]
		if current <= 9:
			result.append(str(current))
			current = 0
		else:
			result.append(str(current % 10))
			current = current // 10
	if current > 0:
		result.append(str(current))
	result.reverse()
	print(''.join(result))


if __name__ == "__main__":
	main()
