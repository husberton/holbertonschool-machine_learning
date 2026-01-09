#!/usr/bin/env python3
""" Statistical analysis """


def analyze(df):
    """ Remove timestamp and describe the data statistically """
    return df.loc[:, "Open": "Weighted_Price"].describe()
