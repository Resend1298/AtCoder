def main():
	_ = int(input())
	s = input().split()

	result = []
	for i in s:
		match i[0]:
			case 'a' | 'b' | 'c':
				result.append('2')
			case 'd' | 'e' | 'f':
				result.append('3')
			case 'g' | 'h' | 'i':
				result.append('4')
			case 'j' | 'k' | 'l':
				result.append('5')
			case 'm' | 'n' | 'o':
				result.append('6')
			case 'p' | 'q' | 'r' | 's':
				result.append('7')
			case 't' | 'u' | 'v':
				result.append('8')
			case 'w' | 'x' | 'y' | 'z':
				result.append('9')

	print(''.join(result))


if __name__ == "__main__":
	main()
