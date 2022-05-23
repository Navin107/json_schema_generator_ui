import os
from subprocess import call,Popen,PIPE

cmd = "pyinstaller --onefile -w json_schema_generator.py"
process = Popen(cmd, shell=True)
process.communicate ()
