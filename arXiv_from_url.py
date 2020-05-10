import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
import glob
import tarfile
import shutil
import requests
from optparse import OptionParser

def split_filename(filename="../temp_20200408000/not_ignore.txt"):
    name = os.path.basename(filename)
    dir_name = os.path.dirname(filename)
    sub_name = os.path.basename(os.path.dirname(filename))
    rootname, ext_name = os.path.splitext(name)
    return name, dir_name, sub_name

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--tar", dest="tar", default="../../Downloads/1908.03795")
    parser.add_option("--url", dest="url", default="https://arxiv.org/e-print/2005.03337")
    parser.add_option("--name", dest="name", default="2005.03337")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    URL = "https://arxiv.org/e-print/" + opt.name
    filename, url_name, sub_name = split_filename(URL)
    print(URL)
    res = requests.get(URL, stream=True)
    tar_file = "./tmp/" + filename
    with open(tar_file, 'wb') as fp:
        shutil.copyfileobj(res.raw, fp)

    basename = os.path.basename(tar_file)
    base_dir = "arXiv." + basename
    dirnum = len(glob.glob(base_dir))
    print(basename)
    print(dirnum)
    if dirnum == 0:
        os.makedirs("arXiv." + basename)
    
    print(os.getcwd())
    #os.chdir(base_dir)
    tar = tarfile.open(tar_file, "r")
    tar.extractall(base_dir)
