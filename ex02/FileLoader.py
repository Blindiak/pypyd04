import pandas as p


class FileLoader:

    @staticmethod
    def load(path):
        data = p.read_csv(path)
        s = data.shape
        print("Loading dataset of dimensions", s[0], "x", s[1])
        return data

    @staticmethod
    def display(df, n):
        print(df.head(n))


if __name__ == "__main__":
    from ProportionBySport import proportionBySport

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
