#!/usr/bin/env python3
'''

python -m unittest test_cangw
python -m unittest test_cangw.test_cangw.test_cangw_forward_on
python -m unittest test_cangw.test_cangw.test_cangw_forward_off

'''
import os
import sys
from time import time, sleep                                                                      
import struct                                                                                     
import argparse                                                                                   
import contextlib                                                                                 
import io                                                                                         
import unittest
                                                                                                  
from prompt_toolkit import PromptSession                                                          
from prompt_toolkit.history import FileHistory                                                    
from panda import Panda


class test_cangw(unittest.TestCase):

	def test_cangw_forward_on(self):

		print("TestCase:",sys._getframe().f_code.co_name)

		panda = Panda()
		
		speed_kbps = 500
		
		for bus in range(3):
		    panda.set_can_speed_kbps(bus, speed_kbps) 
		    panda.set_can_forwarding(bus, -1)   #disable all forwarding
		    
		panda.set_safety_mode(Panda.SAFETY_CANGW) 
		
		panda.set_can_forwarding(0,2)
		panda.set_can_forwarding(2,0)
		
		panda.close()
		
	
	def test_cangw_forward_off(self):

		print("TestCase:",sys._getframe().f_code.co_name)
	
		panda = Panda()
		
		speed_kbps = 500
		
		for bus in range(3):
		    panda.set_can_speed_kbps(bus, speed_kbps) 
		    panda.set_can_forwarding(bus, -1)   #disable all forwarding
		    
		panda.set_safety_mode(Panda.SAFETY_CANGW) 
		
		panda.set_can_forwarding(0,-1)
		panda.set_can_forwarding(2,-1)
		
		panda.close()
	
if __name__ == "__main__":
    unittest.main()
