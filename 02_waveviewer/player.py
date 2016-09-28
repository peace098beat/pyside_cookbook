import sys
import time
import threading
import pyaudio

class Player(object):
    def __init__(self, buffer, chunk_size=None, rate=None, live=None):
        self.rate = rate
        self.buffer_size = buffer.size / 2
        assert chunk_size < self.buffer_size
        assert buffer.dtype == np.float32
        self.buffer = buffer
        self.chunk_size = chunk_size
        self.live = live
        self.paused = False
    
    def _swap_buffers(self):
        if self.live:
            b0 = self.buffer[:self.buffer_size]
        else:
            b0 = np.zeros(self.buffer_size, dtype=np.float32)
        self.buffer[:self.buffer_size], self.buffer[self.buffer_size:] = self.buffer[self.buffer_size:], b0
            
    def _play_chunk(self):
        chunk = self.buffer[self.i:self.i + self.chunk_size]
        self.stream.write(chunk.tostring())
        self.i += self.chunk_size
        if self.i >= self.buffer_size:
            self.i -= self.buffer_size
            self._swap_buffers()
        
    def _play(self):
        # Open the stream on the background thread.
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=self.rate, output=1)
        if self.paused:
            self.paused = False
        while not self.paused:
            self._play_chunk()
        
    def play(self):
        if not hasattr(self, '_thread'):
            self.i = 0
            self._thread = threading.Thread(target=self._play)
            self._thread.daemon = True
            self._thread.start()
        
    def pause(self):
        self.paused = True
        time.sleep(2 * float(self.chunk_size) / self.rate)
        self.stream.close()
        self._thread.join()
        del self._thread

    def get_nowframe(self):
    	return self.i

    def get_audio(self):
    	return self.buffer

if __name__ == '__main__':
	import numpy as np
	rate = 44100
	buffer_duration = 1.
	buffer_size = int(buffer_duration * rate)
	chunk_size = 1024
	buffer = np.zeros(2 * buffer_size, dtype=np.float32)
	t = np.linspace(0., 2 * buffer_duration, 2 * buffer_size)
	f0 = 440.
	x = np.sin(2 * np.pi * f0 * t) * .1
	buffer[:] = x

	p = Player(buffer, chunk_size=chunk_size, rate=rate, live=True)
	p.play()
	p.pause()
