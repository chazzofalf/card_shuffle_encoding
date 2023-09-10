import sys
class ranks_callable(sys.modules[__name__].__class__):
	def __call__(self):
		return [g for f in [['ace'],[f'{h}' for h in range(2,11)],['jack','queen','king']] for g in f]

sys.modules[__name__].__class__ = ranks_callable
