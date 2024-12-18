import subprocess
scripts = [
    ("RS Checksum Calculator v0.py", ['0']),
]
for i in range(1, 10):
    scripts.append(("RS Checksum Calculator v0.py", [str(i)]))

for script, args in scripts:
    subprocess.Popen(["python", script] + args)