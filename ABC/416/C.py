# TODO: review

from itertools import product


def main():
	n, k, x = [int(i) for i in input().split()]
	s = [input() for _ in range(n)]

	# s.sort()
	#
	# set_s = list(set(s))
	# set_s.sort()
	#
	# if len(set_s) == n:
	# 	tmp = 0
	# 	for i in product(range(n), repeat=k):
	# 		tmp += 1
	# 		if tmp == x:
	# 			result = i
	# 			break
	#
	# 	result_str = []
	# 	for i in result:
	# 		result_str.append(s[i])
	# 	print(''.join(result_str))
	#
	# else:
	# 	count = {}
	# 	for i in s:
	# 		if i in count:
	# 			count[i] += 1
	# 		else:
	# 			count[i] = 1
	#
	# 	tmp = 0
	# 	for i in product(range(len(set_s)), repeat=k):
	# 		tmp_1 = 1
	# 		for j in i:
	# 			tmp_1 *= count[set_s[j]]
	# 		tmp += tmp_1
	#
	# 		if tmp >= x:
	# 			result = i
	# 			break
	#
	# 	result_str = []
	# 	for i in result:
	# 		result_str.append(set_s[i])
	# 	print(''.join(result_str))

	all_s = []
	for i in product(range(n), repeat=k):
		tmp = []
		for j in i:
			tmp.append(s[j])
		all_s.append(''.join(tmp))
	all_s.sort()
	print(all_s[x - 1])


if __name__ == "__main__":
	main()
