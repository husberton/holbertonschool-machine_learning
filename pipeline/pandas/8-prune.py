#!/usr/bin/env python3
""" Remove empty elements in close """


def prune(df):
    """ Input: DataFrame, Output: 'pruned' DataFrame """
    return df.dropna(subset="Close")
