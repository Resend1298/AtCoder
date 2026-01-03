SOLVE_FILE = "../ABC/123/A.py"

import subprocess
import sys


def main():
	while True:
		with open("test_data.in", "w") as f:
			subprocess.run([sys.executable, "gen.py"], stdout=f)

		with open("test_data.in") as f_in, open("test_data_solve.out", "w") as f_out:
			subprocess.run([sys.executable, SOLVE_FILE], stdin=f_in, stdout=f_out)
		with open("test_data.in") as f_in, open("test_data_bf.out", "w") as f_out:
			subprocess.run([sys.executable, "bf.py"], stdin=f_in, stdout=f_out)

		with open("test_data_solve.out") as f1, open("test_data_bf.out") as f2:
			assert f1.read() == f2.read()


if __name__ == "__main__":
	main()
