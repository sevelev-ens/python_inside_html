# format : python render.py input.html output.html
from PythonInsideHTML import PIH
import sys
exec(PIH(sys.argv[1]).pythonCode())
with open(sys.argv[2], "w") as fout: fout.write(py_code.getvalue())
