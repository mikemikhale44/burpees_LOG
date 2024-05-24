# Importing libraries
import pandas as pd
import numpy as np

# Creating the base DateFrame
columns_names = ['TotalBurpees', 'BurpeesVariation', 'TotalPush-ups', 'TotalTime']
burpees_log = pd.DataFrame(index=pd.date_range('2024-05-20', end='2024-05-26', freq='D'), columns=columns_names)

# Update columns
burpees_log['TotalBurpees'] = [100, 300, 100, 300, 100, 0, 0]
burpees_log['BurpeesVariation'] = ['6CT', 'NS', '6CT', 'NS', '6CT', 'NS', 'NS']
burpees_log['TotalPush-ups'] = [100, 100, 100, 100, 100, 100, 100]

# Update column TotalTime
burpees_log.iloc[1, 3] = '23:37'
burpees_log.iloc[3, 3] = '23:27'

print(burpees_log)