# -*- coding: utf-8 -*-
"""
Example script to test connection with DATAPixx      

@author: Guillermo Aguilar, Dec 2017
"""

import time
import sys
sys.path.insert(0, "../build/dist-packages")

import datapixx as dpx

# Open datapixx.
datapixx = dpx.open()

# set videomode: Concatenate Red and Green into a 16 bit luminance
# channel.
datapixx.setVidMode(dpx.DPREG_VID_CTRL_MODE_M16)

# Demonstrate successful initialization with button blinks
datapixx.blink(dpx.BWHITE)

datapixx.blink(dpx.BWHITE | dpx.BBLUE | dpx.BGREEN
            | dpx.BYELLOW | dpx.BRED)
                        
datapixx.blink(dpx.BBLUE | dpx.BGREEN | dpx.BYELLOW | dpx.BRED)


# closes
datapixx.close()
