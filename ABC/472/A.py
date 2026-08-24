# TODO: review

def main():
	s = input()

	result = []
	for i in s:
		if i != 'A':
			result.append('.')
		else:
			result.append(i)

	print(''.join(result))


if __name__ == "__main__":
	main()
