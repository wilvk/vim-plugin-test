from subprocess import Popen, PIPE
from time import sleep
import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/plugin")
from nbstreamreader import NonBlockingStreamReader as NBSR

def start_process():
    return Popen(['gdb'], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True, close_fds=True)

def read_stdout(nbsr, print_output=True):
    while True:
        output = nbsr.readline(0.1)
        if not output:
            break
        if print_output:
            print(output.decode("utf-8"))

process = start_process()
nbsr = NBSR(process.stdout)
read_stdout(nbsr)
process.communicate(input=b'help\n')
read_stdout(nbsr)
