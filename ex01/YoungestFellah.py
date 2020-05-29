import pandas as p

def youngestFellah(data, year):
    info = data.loc[data['Year'] == year and data['Sex'] == 'M']
    m = info.loc[info['Sex'] == 'M']
    f = info.loc[info['Sex'] == 'F']
    y_m = m['Age'].min()
    y_f = f['Age'].min()
    return {'f': y_f, 'h': y_m}
