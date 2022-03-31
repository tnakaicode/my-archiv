import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
import tarfile
import argparse

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", dest="dir", default=None)
    parser.add_argument("--name", dest="name", default="DailyReport")
    opt = parser.parse_args()
    print(opt, argvs)

    tar = tarfile.open(tar_name, "w")
    tar.add("./src/")
    tar.close()
    #
    # python -m tarfile -c monty.tar  spam.txt eggs.txt
    # python -m tarfile -c monty.tar life-of-brian_1979/
    # python -m tarfile -e monty.tar
    # python -m tarfile -e monty.tar  other-dir/
    # python -m tarfile -l monty.tar
    # 
    # Compression
    # tar -zcvf filename.tar.gz directoryname
    #
    # Thaw
    # tar -zxvf filename.tar.gz
    #