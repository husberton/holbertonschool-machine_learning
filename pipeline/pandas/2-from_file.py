#!/usr/bin/env python3
"""file -> dataframe"""
import pandas as pd


def from_file(filename, delimiter):
    """
    function input -> filename, delimiter
    function output -> dataframe
    """
    return pd.read_csv(filename, delimiter=delimiter)
