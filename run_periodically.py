
import time
import subprocess
import sys

while True:
    subprocess.run([sys.executable, "Simple_interest.py"])
    print("Program executed. Next run in 3 minutes.")
    time.sleep(180)
