import sys
import cards
import math
class get_unscramble_callable(sys.modules[__name__].__class__):
	def __call__(self,shuffle):
		my_cards=cards()
		my_cards_len=len(my_cards)
		max_number=math.factorial(my_cards_len)
		pick_idxs=[]
		for f in shuffle:
			pick_idx=my_cards.index(f)
			pick_idxs.append(pick_idx)
			del my_cards[pick_idx]
			print(len(my_cards))
		pick_idxs = pick_idxs[:-1]
		print(pick_idxs)
		print(len(pick_idxs))
		m=max_number//my_cards_len
		rv=0
		tg=51
		for f in pick_idxs:
			rv += f*m
			m //= tg
			tg -= 1
		return rv
	
		

sys.modules[__name__].__class__=get_unscramble_callable
