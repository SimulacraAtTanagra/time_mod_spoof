# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:15:23 2021

@author: shane
"""

import os 
from datetime import datetime as dt


def time_mod_spoof(fileloc,datestr=None,year=None,month=None,day=None):
    """
    datestr should be in 'month/day/year' format.
    year,month,day should be in minimum digit int format like 2020,1,1
    """
    if datestr:
        time=dt.strptime(datestr,'%m/%d/%Y').timestamp()
    else:
        year=int(year)
        month=int(month)
        day=int(day)
        time=dt(year,month,day,0,0).timestamp()
    stinfo = os.stat(fileloc)
    os.utime(fileloc,(stinfo.st_atime, time))
    
    
    