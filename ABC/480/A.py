# TODO: review

def main():
	s = [input() for _ in range(2)]

	for i in range(2):
		for j in range(2):
			match s[i][j]:
				case 'A':
					ax, ay = i, j
				case 'D':
					dx, dy = i, j

	if abs(ax - dx) + abs(ay - dy) == 1:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
