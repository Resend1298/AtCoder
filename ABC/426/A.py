# TODO: review

def main():
	version = ["Ocelot", "Serval", "Lynx"]
	x, y = input().split()

	if version.index(x) >= version.index(y):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
