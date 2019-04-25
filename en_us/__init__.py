#!/bin/python3
import os
import logging
from optparse import Values
import SequiturTool
from sequitur import Translator
from functools import lru_cache
logger = logging.getLogger()
__dict_path__ = os.path.join(os.path.dirname(__file__), 'cmudict', 'cmudict.dict')
__model_path__ = os.path.join(os.path.dirname(__file__), 'models', 'order-9')

try:
    from .. en_gb import G2P as G2P_base
except:
    from en_gb import G2P as G2P_base

class G2P(G2P_base):

    def __init__(self, dict_path=__dict_path__, model_path=__model_path__):
        super().__init__(dict_path=__dict_path__, model_path=__model_path__)

if __name__ == '__main__':
    g2p = G2P()
    print(g2p['hello'])
    print(g2p['github'])