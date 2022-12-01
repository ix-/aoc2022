import pandas as pd


class SearchParty:
    def __init__(self, filename):
        self.filename = filename
        self.data = filename

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, filename):
        self._data =  pd.read_csv(filename, names=["calories"], skip_blank_lines=False)
        self.data["elf"] = self.data["calories"].isna().cumsum()

    def task_1_1(self):
        grp = self.data.groupby("elf")
        self.calories_per_elf = grp["calories"].sum()
        return self.calories_per_elf.max()

    def task_1_2(self):
        sorted_elves = self.calories_per_elf.sort_values(ascending=False)
        return sorted_elves.head(3).sum()
