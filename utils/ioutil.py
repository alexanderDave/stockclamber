#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import pickle
import os


def save_pickle(item, path):
    with open(path, 'wb') as f:
        print(path)
        pickle.dump(item, f)


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def get_save_path():
    abspath = os.path.dirname(__file__)
    parentpath = os.path.dirname(abspath)
    save_path = os.path.join(parentpath, 'dates')

    return save_path

