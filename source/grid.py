from Melodie import Grid, Spot
from source import data_info


class CovidSpot(Spot):
    def setup(self):
        self.stay_prob = 0.0


class CovidGrid(Grid):
    def setup(self):
        self.set_spot_property("stay_prob", self.scenario.get_matrix(data_info.grid_stay_prob))

