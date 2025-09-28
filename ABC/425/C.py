# TODO: review

def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	shift = 0
	sum_a = [a[0]]
	for i in range(1, n):
		sum_a.append(sum_a[-1] + a[i])

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case [1, c]:
				shift += c
				shift %= n
			case [2, l, r]:
				l -= 1
				r -= 1
				l += shift
				r += shift
				l %= n
				r %= n
				if l <= r:
					print(sum_a[r] - sum_a[l - 1] if l > 0 else sum_a[r])
				else:
					print(sum_a[r] + sum_a[-1] - sum_a[l - 1])


if __name__ == "__main__":
	main()
