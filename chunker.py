import sys
import cards
import math
import dumb_bytes
class chunker_callable(sys.modules[__name__].__class__):
	def __call__(self,byteslike):
		max_value=math.factorial(len(cards()))-1
		dumb_max_value=dumb_bytes(max_value)
		max_len=len(dumb_max_value)-1
		chunksize=max_len
		chunks=[]
		byteslikerw=byteslike
		while len(byteslikerw) > 0:
			chunks.append(bytes(byteslikerw[:chunksize]))
			byteslikerw = byteslikerw[chunksize:]
		return	chunks

sys.modules[__name__].__class__ = chunker_callable
