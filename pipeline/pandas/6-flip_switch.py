#!/usr/bin/env python3
""" Transposing a DataFrame """


def flip_switch(df):
    """ Input: DataFrame, Output: Transposed DataFrame """
    df.sort_values(by="Timestamp", ascending=False, inplace=True)
    return df.T
