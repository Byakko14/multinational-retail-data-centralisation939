import subprocess

# Run the java command to get Java version
java_version = subprocess.run(['java', '-version'], stderr=subprocess.PIPE).stderr.decode('utf-8')

print(java_version)