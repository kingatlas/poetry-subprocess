import subprocess
import sys
import pandas
print("main program, pandas version:", pandas.__version__)

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
python_cmd = os.path.join(dir_path, "sub-process", ".venv/bin/python")
result = subprocess.run(
    f"bash -c '{python_cmd} sub.py'", capture_output=True, shell=True, cwd="sub-process"
)
print(str(result.stdout))
