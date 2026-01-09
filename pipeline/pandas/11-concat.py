#!/usr/bin/env python3
import pandas as pd
""" Concatenate to DataFrames """
index = __import__('10-index').index


def concat(df1, df2):
    """ Input: twp DFs, Output: one concatenated DF """
    df1 = index(df1)
    df2 = index(df2)
    df = pd.concat([df2.loc[:1417411920], df1], keys=["bitstamp", "coinbase"])
    return df
