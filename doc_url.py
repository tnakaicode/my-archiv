import os
import sys
import time
import glob
import shutil
import requests
import datetime
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
    parser.add_option("--url", dest="url",
                      default='https://link.springer.com/content/pdf/10.1007%2F978-3-642-28255-3_4.pdf')
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    URL = opt.url
    name, url_name, sub_name = split_filename(URL)
    print(URL)
    res = requests.get(URL, stream=True)
    with open("./archive/" + name, 'wb') as fp:
        shutil.copyfileobj(res.raw, fp)
