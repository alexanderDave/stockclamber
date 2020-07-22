#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import pickle


def save_pickle(item, path):
    with open(path, 'wb') as f:
        pickle.dump(item, f)


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)