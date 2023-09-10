import sys
import dechunker
import dumb_bytes
class dumb_dechunker(sys.modules[__name__].__class__):
	def __call__(self,smart_chunks):
		return bytes([x for f in smart_chunks for x in dumb_bytes(f)])

sys.modules[__name__].__class__ = dumb_dechunker
