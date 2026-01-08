#!/usr/bin/env python3
""" This script modifies a DataFrame """
import pandas as pd
import datetime as dt


def rename(df):
     '''
    Renames Timestamp to Datetime, converts to datetime,
    and keeps only Datetime and Close columns.

    :param df: pd.DataFrame
    :return: modified pd.DataFrame
    '''

    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = dt.datetime.fromtimestamp(df["Datetime"])
    return df.loc[["Datetime", "Close"]]
