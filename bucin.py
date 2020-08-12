# -*- coding: utf-8 -*-
import sys,time
def jalan (kata):
	for e in kata:
		sys.stdout.write(e)
		sys.stdout.flush()
                time.sleep(0.09)

print jalan( '\033[92m Aku ingin mencintaimu dengan sederhana' .center(1))
print jalan( 'dengan kata yang tak sempat diucapkan kayu' .center(1))
print jalan( 'kepada api yang menjadikannya abu' .center(1))

print jalan( 'Aku ingin mencintaimu dengan sederhana' .center(1))
print jalan( 'dengan isyarat yang tak sempat disampaikan' .center (1))
print jalan( 'awan kepada hujan yang menjadikannya tiada' .center(1))
