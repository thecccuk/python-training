import pandas as pd
def MeanInt(D):
 x=D['space_heating_co2']/D['floor_area']
 return x.mean()
DF=pd.read_csv('buildings.csv')
print( MeanInt(DF) )
