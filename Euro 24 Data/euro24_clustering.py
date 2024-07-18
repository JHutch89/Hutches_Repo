from statsbombpy import sb
import pandas as pd
import inspect

def options():
    # This is allowing me to show all columns/column headers
    pd.set_option('display.max_columns', None)
    # This is allowing me to show all rows
    pd.set_option('display.max_rows', None)
    # This is allowing me to keep all columns on one line
    pd.set_option('expand_frame_repr', False)

options()

# euro_data = sb.matches(competition_id=55, season_id=282)
# print(euro_data.head(20))

# argspec = inspect.getfullargspec(sb.matches)
# print("Parameters for sb.matches():")
# print("Arguments:", argspec.args)
# print("Varargs:", argspec.varargs)
# print("Keywords:", argspec.varkw)
# print("Defaults:", argspec.defaults)
competitions = sb.competitions()
print(competitions[['competition_id', 'competition_name']])