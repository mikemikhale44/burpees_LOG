# Importing libraries
import pandas as pd
import numpy as np

# Creating the base DateFrame
columns_names = ['TotalBurpees', 'BurpeesVariation', 'TotalPush-ups', 'TotalTime']
burpees_log = pd.DataFrame(index=pd.date_range('2024-05-20', end='2024-05-26', freq='D'), columns=columns_names)

print(burpees_log)