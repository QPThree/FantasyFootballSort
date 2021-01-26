
# Work with Pandas and data munging
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fantasydatapros/data/master/fantasypros/fp_projections.csv')

#iloc shows us which [columns, rows] to look at.  In this case, all columns, and all but the first row
df = df.iloc[:, 1:]

#defining columns we care to see
base_columns = ['Player', 'Team', 'Pos']
QB_columns = ['PassingAtt', 'PassingCmp', 'PassingTD', 'FantasyPoints']
WR_columns = ['Receptions', 'ReceivingYds', 'ReceivingTD']

# 'Pos' could be changed, would have to add that positions relative columns
# New dataframe is made of just QB's
qb_df = df.loc[(df['Pos'] == 'QB'), base_columns + QB_columns]
wr_df = df.loc[(df['Pos'] == 'WR'), base_columns + WR_columns]

#Can change the 'by' to sort by preferred category
#print(qb_df.sort_values(by = 'PassingAtt', ascending = False).head(10))
print(wr_df.sort_values(by = 'ReceivingTD', ascending = False).head(25))


