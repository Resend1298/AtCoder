# TODO: review

def main():
	n = int(input())

	result = []
	for i in range(n, 0, -1):
		result.append(str(i))
		result.append(',')
	del result[-1]

	print(''.join(result))


if __name__ == "__main__":
	main()
