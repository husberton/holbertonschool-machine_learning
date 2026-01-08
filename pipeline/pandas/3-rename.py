#!/usr/bin/env python3
""" This script modifies a DataFrame """
import pandas as pd


def rename(df):
     '''
    Renames Timestamp to Datetime, converts to datetime,
    and keeps only Datetime and Close columns.

    :param df: pd.DataFrame
    :return: modified pd.DataFrame
    '''
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit=s)
    df = df[["Datetime", "Close"]]
    return df
