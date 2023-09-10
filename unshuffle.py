import sys
import get_unscramble
# alias for get_unscramble
class unshuffle_callable(sys.modules[__name__].__class__):
	def __call__(self,idx):
		return get_unscramble(idx)

sys.modules[__name__].__class__ = unshuffle_callable
