
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))

def execute_code(code):
	f = open("{}/build/temp.b".format(path),"w")
	f.write(code)
	f.close()

	os.system("{} {}/build/temp.b".format(sys.argv[1],path))


execute_code("""
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
""")