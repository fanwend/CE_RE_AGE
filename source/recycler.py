from typing import TYPE_CHECKING

from Melodie import Agent

if TYPE_CHECKING:
    from .scenario import CEScenario


# 在model里注册agent，在enviroment里写不同agent1的互动

class Recycler(Agent):
    scenario: "CEScenario"

    def setup(self):
        self.landfill_product = 0
        self.init_r_choice = 0

    def landfill_cal(self):
        self.landfill_product = 1
        return self.landfill_product
