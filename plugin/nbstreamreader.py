'''
  Taken from http://eyalarubas.com/python-subproc-nonblock.html
'''

from threading import Thread
from queue import Queue, Empty

class NonBlockingStreamReader(object):
    def __init__(self, stream):
        self._s = stream
        self._q = Queue()

        def populateQueue(stream, queue):
            while True:
                if not stream.closed:
                    line = stream.readline()
                    if line:
                        queue.put(line)
                    else:
                        print()

        self._t = Thread(target = populateQueue, args = (self._s, self._q))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def readline(self, timeout = None):
        try:
            return self._q.get(block = timeout is not None, timeout = timeout)
        except Empty:
            return None

