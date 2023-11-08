import pandas as pd
import df_options

df_options.options()

epl = pd.read_csv('/Users/jasonhutches/Desktop/Jason Hutches/Hutches_Repo/CSVs/premier_league_all_matches.csv')

print(epl.head())