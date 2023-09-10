import sys
class suits_callable(sys.modules[__name__].__class__):
	def __call__(self):
		return [f for f in ['hearts','spades','diamonds','clubs']]

sys.modules[__name__].__class__ = suits_callable
