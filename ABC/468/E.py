from math import ceil

MOD = 998244353


# noinspection GrazieInspection
def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	# Take n=5, a=[a1, a2, a3, a4, a5] for example,
	# result = 1/1(a1+a2+a3+a4+a5)
	#        + 1/2(a1+2a2+2a3+2a4+a5)
	#        + 1/3(a1+2a2+3a3+2a4+a5)
	#        + 1/4(a1+2a2+2a3+2a4+a5)
	#        + 1/5(a1+a2+a3+a4+a5) (% MOD)
	# then, we can see that:
	# 1. 1/1 and 1/5 give the same bracket, 1/2 and 1/4 give the same bracket, and so on.
	# 2. a1+2a2+2a3+2a4+a5 = a1+a2+a3+a4+a5(previous bracket) + a2+a3+a4(can be calculated by prefix sum), and so on.
	# 3. 1/1(a1+a2+a3+a4+a5) % MOD can be calculated by using a/b % p = a * b**(p-2) % p

	result = 0
	a_prefix_sum = [0]
	for i in a:
		a_prefix_sum.append(a_prefix_sum[-1] + i)
	current_a_sum = 0

	for i in range(1, ceil(n / 2) + 1):
		current_a_sum += a_prefix_sum[-i] - a_prefix_sum[i - 1]
		result += (current_a_sum % MOD) * pow(i, MOD - 2, MOD)
		result %= MOD

		if n - i + 1 != i:
			i = n - i + 1
			result += (current_a_sum % MOD) * pow(i, MOD - 2, MOD)
			result %= MOD

	print(result)


if __name__ == "__main__":
	main()
