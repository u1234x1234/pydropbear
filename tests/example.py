from pysshserver import SSHServer
import time


with SSHServer():
    time.sleep(10)
