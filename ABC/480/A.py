def main():
	s = [input() for _ in range(2)]

	if {s[0][0], s[1][1]} == {'A', 'D'} or {s[0][1], s[1][0]} == {'A', 'D'}:
		print("No")
	else:
		print("Yes")


if __name__ == "__main__":
	main()
