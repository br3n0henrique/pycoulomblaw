# Developed by Breno Henrique da Silva, a high school student at the
# Federal Institute of Education, Science and Technology of São Paulo - Campus Catanduva
import pandas as pd
from scipy.constants import epsilon_0

k = (epsilon_0)
print('The permittivity of vacuum is: ', k)
dataframe = pd.DataFrame(columns=['Charge 1 (Coulomb)', 'Charge 2 (Coulomb)', 'Distance (Meter)', 'Force (Newton)'])
dataframe.index.names = ['Number']
i=0
choose=1
while (choose!=0):
    print('\n[Row {}]'.format(i))
    #get the values of charges and distannces
    c1 = float(input('Enter the modular value of charge 1 in Coulomb: '))
    c2 = float(input('Enter the modular value of charge 2 in Coulomb: '))
    d = float(input('Enter the value of the distance between charges in meters: '))
    teste = str(input('To stop, type "s": '))
    #verify if the user wants to continue
    if (teste == 's'):
        choose=0
    #calculate the force between charges
    f = (k * c1 * c2)/(d * d)
    #write info into a dataframe
    dataframe.loc[i] = [c1, c2, d, f]  # adding a row
    #go to the next row
    i=i+1

#get data from the while condition
dataframe = pd.DataFrame(data=dataframe)
print('___________________________________________________________________')
#print and export table
print(dataframe)
dataframe.to_csv('table.csv')
print('___________________________________________________________________')
print('\n *****Table exported to "table.csv"****')