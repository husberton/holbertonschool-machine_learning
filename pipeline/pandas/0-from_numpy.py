#!/usr/bin/env python3
""" This module uses pandas"""
import pandas as pd


def from_numpy(array):
    """ This function comver numpy array into pandas dataframe"""
    letters = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=letters)
