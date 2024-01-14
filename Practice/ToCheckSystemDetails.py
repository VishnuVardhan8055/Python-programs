# ---> To Check the present version of using Python
import sys
print("Python Version :", sys.version)
#from subprocess import java_version
#print("Python by platform :",java_version())
import subprocess
version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
print(version)
import os
import platform
import sysconfig
print("OS name:", os.name)
print("Platform :",platform.system())
print("Version of OS release;",platform.release())
print("architecutre:",platform.architecture())
print("Platfrom:",sysconfig.get_platform())
print("platform Machine:",platform.machine())