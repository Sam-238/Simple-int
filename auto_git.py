
import time
import subprocess

while True:
    subprocess.run(["git", "add", "."])

    result = subprocess.run([
        "git", "commit", "-m", "Automatic update"
    ])

    if result.returncode == 0:
        subprocess.run(["git", "push", "origin", "main"])

    print("Waiting 3 minutes...")
    time.sleep(180)

