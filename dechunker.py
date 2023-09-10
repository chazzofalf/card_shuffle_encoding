import sys
class dechunker_callable(sys.modules[__name__].__class__):
	def __call__(self,chunks):
		out=bytearray([])
		for chunk in chunks:
			out.extend(chunk)
		return bytes(out)

sys.modules[__name__].__class__ = dechunker_callable
