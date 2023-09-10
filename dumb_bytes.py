import sys
class dumb_bytes_callable(sys.modules[__name__].__class__):
	def __call__(self,smart_bytes_int):
		guessed_size=0
		guessed_min=0
		last_guessed_min=None
		while guessed_min<smart_bytes_int:
			last_guessed_min = guessed_min
			guessed_min += (256**guessed_size)
			guessed_size += 1
		if guessed_min>smart_bytes_int:
			guessed_min=last_guessed_min
			guessed_size -= 1
		rv=smart_bytes_int-guessed_min
		out=bytearray([])
		for f in range(0,guessed_size):
			out.insert(0,rv % 256)
			rv //= 256
		return bytes(out)

sys.modules[__name__].__class__ = dumb_bytes_callable
