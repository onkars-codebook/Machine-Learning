import  pandas as pd
import numpy as np

file = pd.read_csv("List.csv");
file["Name"][2] = "Trupti"

print(file)
