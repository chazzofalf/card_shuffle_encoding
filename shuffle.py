import sys
import get_scramble
# alias for get_scramble
class shuffle_callable(sys.modules[__name__].__class__):
	def __call__(self,idx):
		return get_scramble(idx)

sys.modules[__name__].__class__ = shuffle_callable
