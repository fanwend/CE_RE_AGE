from typing import TYPE_CHECKING

from Melodie import Model, Network

from source import data_info
from source.agent import CEAgent
from source.data_collector import CovidDataCollector
from source.environment import CEEnvironment
from source.grid import CovidGrid, CovidSpot
from source.recycler import Recycler #这部分的语法是文件中的类
from source.scenario import CEScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class CEModel(Model):
    scenario: CEScenario

    def create(self):
        self.agents: "AgentList[CEAgent]" = self.create_agent_list(CEAgent)
        self.recycleagents = self.create_agent_list(Recycler)
        self.environment: "CEEnvironment" = self.create_environment(CEEnvironment)
        self.data_collector = self.create_data_collector(CovidDataCollector)
        self.grid = self.create_grid(CovidGrid, CovidSpot)
        self.network = self.create_network()

    def setup(self):#这里注册模型的常数
        self.agents.setup_agents(
            agents_num=self.scenario.agent_num,
            params_df=self.scenario.get_dataframe(data_info.agent_params)
        )
        self.recycleagents.setup_agents(
            agents_num=self.scenario.recycle_num,
            params_df=self.scenario.get_dataframe(data_info.recycle_params)
        )
        self.grid.setup_params(width=self.scenario.grid_x_size, height=self.scenario.grid_y_size)
        self.grid.setup_agent_locations(self.agents)
        self.network.setup_agent_connections(
            agent_lists=[self.agents],
            network_type=self.scenario.network_type,
            network_params=self.scenario.get_network_params(),
        )

    def run(self):
        for period in self.iterator(self.scenario.period_num):
            for hour in range(0, self.scenario.period_hours):
                self.environment.agents_move(self.agents)
                self.environment.agents_infection(self.agents)
            self.environment.agents_update_vaccination_trust(self.agents, self.network)
            self.environment.agents_take_vaccination(self.agents)
            self.environment.agents_health_state_transition(self.agents)
            self.environment.calc_population_infection_state(self.agents)
            self.environment.agents_product_waste(self.agents)
            self.environment.agents_total_product(self.agents)
            self.environment.agents_total_pbc(self.agents)
            self.environment.agents_agent_neighbors_norms(self.agents, self.network)
            self.environment.agents_choice_after_cal(self.agents)
            self.environment.agent_difusion_cal(self.agents)
            self.environment.agent_Re_landfill_cal(self.recycleagents)
            self.data_collector.collect(period)
        self.data_collector.save()
