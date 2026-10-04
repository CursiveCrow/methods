import sys
sys.path.insert(0, "tools")
import symbols2tex as t

BS = "\\"
assert t.text_cell("path u_i and " + BS + "(u_i" + BS + ")") == "path u" + BS + "_i and " + BS + "(u_i" + BS + ")"
assert t.text_cell("ok " + BS + "_ 5% & 2^h") == "ok " + BS + "_ 5" + BS + "% " + BS + "& 2" + BS + "^{}h"
assert t.text_cell("$x_1$ and " + BS + "[a_b" + BS + "]") == "$x_1$ and " + BS + "[a_b" + BS + "]"
print("text_cell ok")
