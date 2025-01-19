import pandas as pd 
import sys

print(sys.version)

data = {
    "Namn": ["Erik", "Anna", "Johan", "Lisa", "Oskar"],
    "Ålder": [28, 34, 40, 25, 50],
    "Stad": ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Lund"],
    "Lön": [45000, 32000, 20000, 25000, 30000] 
}


df = pd.DataFrame(data)
print(df)