class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        info = self.data.loc[self.data['City'] == location]
        info = info.drop_duplicates(subset="Year")
        return info.Year.tolist()

    def where(self, date):
        info = self.data.loc[self.data['Year'] == date]
        info = info.drop_duplicates(subset="City")
        return [info['City'].item()]
