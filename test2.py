import subprocess
def runtrace(destination):
    result = subprocess.run(["traceroute", "-I", destination], capture_output=True, text=True)
    print(result.stdout)