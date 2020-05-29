def proportionBySport(data, year, sport, gender):
    info = data.loc[data['Year'] == year]
    g = info.loc[info['Sex'] == gender]
    g_no_dup = g.drop_duplicates(subset="Name", keep='first', inplace=False)
    s = g_no_dup.loc[g_no_dup['Sport'] == sport]
    return len(s) / len(g_no_dup)
