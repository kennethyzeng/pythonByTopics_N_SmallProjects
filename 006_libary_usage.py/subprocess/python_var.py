import subprocess

filepath="test.txt"
shellCmd="cat {0} | sed '2s/.*/this is 4nd line/' > temp.txt && mv temp.txt {0}".format(filepath)
result=subprocess.run(shellCmd, shell=True, capture_output=True, text=True)
print(result.stdout)