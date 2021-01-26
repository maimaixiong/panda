#!/usr/bin/env python3

#Usage:
#	export PYTHONPATH=../..

import os
import sys
from time import time, sleep
#import struct
import argparse
#import contextlib
import io

import argparse
#from prompt_toolkit import PromptSession
#from prompt_toolkit.history import FileHistory
from panda import Panda

import signal


RUN = True
DEBUG = True

def stop_func():
	RUN = False

def cangw_init(panda):
	print("func:",sys._getframe().f_code.co_name)
	panda.set_can_speed_kbps(0, 500)
	panda.set_can_forwarding(0,-1)
	panda.set_can_speed_kbps(1, 500)
	panda.set_can_forwarding(1,-1)
	panda.set_can_speed_kbps(2, 500)
	panda.set_can_forwarding(2,-1)

	panda.set_safety_mode(Panda.SAFETY_CANGW) 


def cangw_on(panda):
	print("func:",sys._getframe().f_code.co_name)
	panda.set_can_forwarding(0,2)
	panda.set_can_forwarding(2,0)


def cangw_off(panda):
	print("func:",sys._getframe().f_code.co_name)
	panda.set_can_forwarding(0,2)
	panda.set_can_forwarding(2,0)

def cangw_rx(panda, bus=[0,1,2]):
	print("func:",sys._getframe().f_code.co_name, "bus:", bus)
	signal.signal(signal.SIGINT, stop_func)
	signal.signal(signal.SIGHUP, stop_func)
	#signal.signal(signal.SIGSTP, stop_func)
	count = 0
	while(RUN):
		msgs = panda.can_recv()
		for can_id, ts, dat, src in msgs:
			count += 1
			if DEBUG and ( src in bus) :
				print(f'RX>{count}\tbus{src}\t{hex(can_id)}:\t0x{dat.hex()}\t{ts}')
		sleep(0.005)
	

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(
			description="set panda to CAN Gateway mode, send data from bus0 to bus2 and from bus2 to bus0",
			formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("-b", "--bus", type=int, nargs="+", default=[0,128,1,129,2,130])

	args = parser.parse_args(sys.argv[1:])

	panda = Panda()
	cangw_init(panda)
	cangw_on(panda)
	cangw_rx(panda, args.bus)
	cangw_off(panda)
	panda.close()
				
	
