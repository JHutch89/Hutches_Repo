import pandas as pd

def options():
    # This is allowing me to show all columns/column headers
    pd.set_option('display.max_columns')
    # This is allowing me to show all rows
    pd.set_option('display.max_rows')
    # This is allowing me to keep all columns on one line
    pd.set_option('expand_frame_repr', False)