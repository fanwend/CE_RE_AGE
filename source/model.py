from typing import TYPE_CHECKING

from Melodie import Model

from source import data_info
from source.agent import CEAgent
from source.data_collector import CovidDataCollector
from source.environment import CEEnvironment
from source.recycler import Recycler  # 这部分的语法是文件中的类
from source.scenario import CEScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class CEModel(Model):
    scenario: "CEScenario"

    def create(self):
        self.agents: "AgentList[CEAgent]" = self.create_agent_list(CEAgent)
        self.recycle_agents = self.create_agent_list(Recycler)
        self.environment: "CEEnvironment" = self.create_environment(CEEnvironment)
        self.data_collector = self.create_data_collector(CovidDataCollector)
        self.network = self.create_network()

    def setup(self):  # 这里注册模型的常数
        self.agents.setup_agents(
            agents_num=self.scenario.agent_num,
            params_df=self.scenario.get_dataframe(data_info.agent_params)
        )
        self.recycle_agents.setup_agents(
            agents_num=self.scenario.recycle_num,
            params_df=self.scenario.get_dataframe(data_info.recycle_params)
        )
        self.network.setup_agent_connections(
            agent_lists=[self.agents],
            network_type=self.scenario.network_type,
            network_params=self.scenario.get_network_params(),
        )

    def run(self):
        for period in self.iterator(self.scenario.period_num):
            self.environment.agents_product_waste(self.agents)
            self.environment.agents_total_product(self.agents)
            self.environment.agents_total_pbc(self.agents)
            self.environment.agents_agent_neighbors_norms(self.agents, self.network)
            self.environment.agents_choice_after_cal(self.agents)
            self.environment.agent_diffusion_cal(self.agents)
            self.environment.agent_Re_landfill_cal(self.recycle_agents)
            self.data_collector.collect(period)
        self.data_collector.save()
