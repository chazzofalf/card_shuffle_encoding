import sys
import suits
import ranks
class cards_callable(sys.modules[__name__].__class__):
	def __call__(self):
		return [f'{g} of {f}' for f in suits() for g in ranks()]

sys.modules[__name__].__class__ = cards_callable
