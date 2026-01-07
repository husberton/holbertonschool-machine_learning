import pandas as pd
import string

def from_numpy(array):
    letters = list(string.ascii_uppercase)
    return pd.DataFrame(array, columns=letters[:len(array[0])])
