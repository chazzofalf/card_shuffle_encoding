import unshuffle
import dumb_dechunker
import sys
class decoder_callable(sys.modules[__name__].__class__):
	def __call__(self,decks):
		return dumb_dechunker([unshuffle(f) for f in decks])

sys.modules[__name__].__class__ = decoder_callable
