"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2



def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()
    print(df.pregnum.value_counts().sort_index())

    ValidatePregnum(df)
    print('%s: All tests passed.' % script)

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    # CleanFemResp(df)
    return df

def ValidatePregnum(df):

    # Gets pregnancy information and creates a map
    # between pregnancy and respondant info through caseid
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    # indexes all the pregnancy numbers from respondnent info
    for index, pregnum in df.pregnum.items():
        # grabs caseid and the indices of each pregnancy
        caseid = df.caseid[index]
        indices = preg_map[caseid]

        # checks if number of indices of pregnancies and
        # pregnum are the same
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False
        return True


if __name__ == '__main__':
    main(*sys.argv)
