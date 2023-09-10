import smart_bytes
import chunker
import sys
class smart_chunker_callable(sys.modules[__name__].__class__):
	def __call__(self,byteslike):
		return [smart_bytes(f) for f in chunker(byteslike)]

sys.modules[__name__].__class__ = smart_chunker_callable
