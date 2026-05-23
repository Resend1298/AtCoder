def main():
	n = int(input())
	s = input().split()

	c = [0] * n
	for i in range(n):
		match s[i][0]:
			case 'a' | 'b' | 'c':
				c[i] = 2
			case 'd' | 'e' | 'f':
				c[i] = 3
			case 'g' | 'h' | 'i':
				c[i] = 4
			case 'j' | 'k' | 'l':
				c[i] = 5
			case 'm' | 'n' | 'o':
				c[i] = 6
			case 'p' | 'q' | 'r' | 's':
				c[i] = 7
			case 't' | 'u' | 'v':
				c[i] = 8
			case 'w' | 'x' | 'y' | 'z':
				c[i] = 9

	print(''.join(str(i) for i in c))


if __name__ == "__main__":
	main()
