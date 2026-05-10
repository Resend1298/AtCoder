# TODO: unsolved

def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	tmp_index = 0
	tmp_min = float("inf")
	for i in range(n):
		if a[i] < tmp_min:
			tmp_min = a[i]
			tmp_index = i

	r = (tmp_index + 1) * k + tmp_min
	l = tmp_min

	while r - l > 1:
		mid = (l + r) // 2

		tmp = 0
		for i in range(n):
			if a[i] < mid:
				div_tmp = (mid - a[i]) // (i + 1)
				while div_tmp * (i + 1) + a[i] < mid:
					div_tmp += 1
				tmp += div_tmp
				if tmp > k:
					r = mid - 1
					break
		else:
			l = mid

	for result in range(r, l - 1, -1):
		tmp = 0
		for i in range(n):
			if a[i] < result:
				div_tmp = (result - a[i]) // (i + 1)
				while div_tmp * (i + 1) + a[i] < result:
					div_tmp += 1
				tmp += div_tmp
				if tmp > k:
					break
		else:
			print(result)
			break


if __name__ == "__main__":
	main()
