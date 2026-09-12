from collections import Counter
from sys import setrecursionlimit


def sieve_of_eratosthenes(n):
	is_prime = [True] * (n + 1)

	for i in range(2, int(n ** 0.5) + 1):
		if is_prime[i]:
			for j in range(i ** 2, n + 1, i):
				is_prime[j] = False

	return [i for i in range(2, n + 1) if is_prime[i]]


def main():
	s = input()

	is_prime = set(sieve_of_eratosthenes(10 ** (len(s))))
	s_counter = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
	index_to_counter_index = [-1] * len(s)
	for i in range(len(s)):
		for j in range(len(s_counter)):
			if s[i] == s_counter[j][0]:
				index_to_counter_index[i] = j
				break

	current = [-1] * len(s_counter)
	used = set()

	def dfs(index):
		if index == len(s_counter):
			current_result = [current[index_to_counter_index[i]] for i in range(len(s))]
			current_result = int(''.join(str(i) for i in current_result))
			if current_result in is_prime:
				print(current_result)
				exit()
			return

		if s_counter[index][0] != s[0]:
			start = 0
		else:
			start = 1

		for i in range(start, 10):
			if i in used:
				continue
			used.add(i)
			current[index] = i
			dfs(index + 1)
			used.remove(i)

	setrecursionlimit(10 ** 7)
	dfs(0)
	print(-1)


if __name__ == "__main__":
	main()
