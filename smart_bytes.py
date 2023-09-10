import sys
class smart_bytes_callable(sys.modules[__name__].__class__):
	def __call__(self,byteslike):
		lenx=len(byteslike)
		if lenx==0:
			return 0
		else:
			skipvalue=0
			for f in range(0,lenx):
				skipvalue += (256**f) 
			rv=0
			for f in byteslike:
				rv *= 256
				rv += f
			rv += skipvalue
			return rv

sys.modules[__name__].__class__ = smart_bytes_callable
