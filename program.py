import decoder
import encoder
import sys
def main():
	if len(sys.argv) == 1:
		do_encode()
	elif len(sys.argv) == 2 and sys.argv[1] == '-d':
		do_decode()
	elif len(sys.argv) == 2 and sys.argv[1] == '-l':
		do_encode(True)
	else:
		raise Exception('Invalid arguments')

def do_encode(dolabels=False):
	
	txt=sys.stdin.read()
	# while block is not None:
		# txt=f'{txt}{block}'
		# block=sys.stdin.read()
	txtb=bytes(txt,encoding='utf8')
	shufs=encoder(txtb)
	# print(shufs)
	deckidx = 1
	for f in shufs:
		if dolabels:			
			sys.stdout.write(f'=== Deck #{deckidx} ===\n')
			sys.stdout.write(f'\n')
		for g in f:
			sys.stdout.write(f'{g}\n')
		deckidx += 1
		if dolabels:
			sys.stdout.write(f'\n')

def do_decode():
	lines=[]
	txt=sys.stdin.read()
	#while block is not None:
	#	lines.append(block.strip())
	#	block=sys.stdin.readline()
	lines=[f for f in txt.split("\n") if len(f) > 0 and not f.startswith("===")]
	#print(lines)
	
	matrix=[]
	while len(lines) > 0:
		matrix.append(lines[:52])
		lines=lines[52:]
	bs=decoder(matrix)
	out=str(bs,encoding='utf8')
	sys.stdout.write(out)

main()

