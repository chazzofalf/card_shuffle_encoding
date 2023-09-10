import sys
import cards
import math
class get_scramble_callable(sys.modules[__name__].__class__):
	def __call__(self,idx):
		maxf=math.factorial(len(cards()))
		maxf //= len(cards())
		my_picks=[]
		my_cards=cards()
		picks_left=len(cards())-1
		while picks_left > 0:
			pick_idx=(idx % math.factorial(picks_left+1)) // math.factorial(picks_left)
			my_picks.append(my_cards[pick_idx])
			del my_cards[pick_idx]
			picks_left -= 1
		my_picks.append(my_cards[0])
		return my_picks

sys.modules[__name__].__class__ = get_scramble_callable
