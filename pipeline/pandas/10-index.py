#!/usr/bin/env python3
""" Set index as the timestamp """


def index(df):
    """ Input: DF, Output: DF with new index """
    return df.set_index(keys="Timestamp")
