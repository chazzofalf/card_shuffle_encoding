import smart_chunker
import shuffle
import sys
class encoder_callable(sys.modules[__name__].__class__):
	def __call__(self,byteslike):
		return [shuffle(f) for f in smart_chunker(byteslike)]

sys.modules[__name__].__class__ = encoder_callable
