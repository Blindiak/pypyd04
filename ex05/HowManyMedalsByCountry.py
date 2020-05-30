def howManyMedalsByCountry(data, name):
    info = data.loc[data['Team'] == name]
    info = info.dropna(subset=['Medal'])
    info = info.sort_values(by=['Year'])
    info = info.drop_duplicates(subset=["Year", "Event"])
    info = info[['Year', 'Medal']]
    info['Medal'] = info['Medal'].str[:1]
    info = info.groupby('Year')['Medal'].apply(list)
    info = info.to_dict()
    for k, v in info.items():
        g = 0
        s = 0
        b = 0
        for m in v:
            if m == 'G':
                g += 1
            if m == 'S':
                s += 1
            if m == 'B':
                b += 1
        info[k] = {'G': g, 'S': s, 'B': b}
    return info