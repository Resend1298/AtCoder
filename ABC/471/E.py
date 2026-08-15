from math import comb

MOD = 998244353


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a_sum = sum(a)
	tmp1 = 0
	tmp2 = 0

	for i in a:
		tmp1 = (tmp1 + i * (a_sum - i)) % MOD
		tmp2 = (tmp2 + i ** 2) % MOD

	result = ((comb(n - 1, k - 1) % MOD) * tmp2) % MOD
	if k >= 2:
		result += ((comb(n - 2, k - 2) % MOD) * tmp1) % MOD
	result %= MOD
	print(result)


if __name__ == "__main__":
	main()
