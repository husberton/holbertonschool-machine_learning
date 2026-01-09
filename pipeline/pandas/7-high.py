#!/usr/bin/env python3
""" Sort by price """


def high(df):
    """ Input: DataFrame, Output: DataFrame sorted high values """
    return df.sort_values(by="High", ascending=False)
