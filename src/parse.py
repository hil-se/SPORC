from pdb import set_trace
import pandas as pd
import urllib3
import time
import random
import os
import numpy as np

qref = 'https://github.com/hil-se/hil-se/blob/main/README.md'
http = urllib3.PoolManager()
req = http.request('GET', qref)
texts = req.data.decode()
print(texts)
