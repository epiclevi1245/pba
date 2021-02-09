import os
import sys
os.system("cmd /c color a")
try:
	os.system("cmd /c pip install websocket")
	print("\n\npip installed websocket")
except:
	print("could not install websocket with pip install websocket, program might not work...")
ip = ""
ncp = ""
cp = ""
jp = ""
nmp = ""
mp = ""
def init(ipa, cpa, jpa, mpa):

	print("PBA REQUIRES NODE.JS to be installed, or an error will occour.\n")
	print("NODE.JS can be installed at\nhttps://nodejs.org/en/download/\n")
	print("Initiating PBA, checking variables...")

	ip = ipa
	ncp = ncpa
	cp = cpa
	jp = jpa
	nmp = nmpa
	mp = mpa

	ipb = open ("ip.txt", "w")
	ipb.write(ipa)
	ipb.close()

	cpb = open ("cp.txt", "w")
	cpb.write(cpa)
	cpb.close()

	jpb = open ("jp.txt", "w")
	jpb.write(jpa)
	jpb.close()

	mpb = open ("mp.txt", "w")
	mpb.write(mpa)
	mpb.close()

	print("wrote data files, waiting for NODE.JS...\n")

	os.system("cmd /c node sendpackets.js")
init("test", "test", "test", "test")