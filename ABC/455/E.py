from collections import Counter


def main():
	n = int(input())
	s = input()

	a_count = 0
	b_count = 0
	c_count = 0
	pre_ab = Counter({0: 1})
	pre_ac = Counter({0: 1})
	pre_bc = Counter({0: 1})
	pre_abc = Counter({(0, 0): 1})
	result_ab = 0
	result_ac = 0
	result_bc = 0
	result_abc = 0

	for i in s:
		match i:
			case 'A':
				a_count += 1
			case 'B':
				b_count += 1
			case 'C':
				c_count += 1

		result_ab += pre_ab[a_count - b_count]
		result_ac += pre_ac[a_count - c_count]
		result_bc += pre_bc[b_count - c_count]
		result_abc += pre_abc[(a_count - b_count, a_count - c_count)]

		pre_ab[a_count - b_count] += 1
		pre_ac[a_count - c_count] += 1
		pre_bc[b_count - c_count] += 1
		pre_abc[(a_count - b_count, a_count - c_count)] += 1

	print(n * (n + 1) // 2 - result_ab - result_ac - result_bc + 2 * result_abc)


if __name__ == "__main__":
	main()
