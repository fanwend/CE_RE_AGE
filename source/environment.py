import random
from typing import TYPE_CHECKING

from Melodie import Environment, AgentList

from source.scenario import CEScenario

if TYPE_CHECKING:
    from Melodie import AgentList
    from source.agent import CEAgent
    from source.recycler import Recycler


class CEEnvironment(Environment):
    scenario: CEScenario

    def agents_product_waste(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.update_wastproduct()

    def agents_total_product(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.total_waste()

    def agents_total_pbc(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.tpb_subjective_norm()

    def agents_agent_neighbors_norms(self,agents: "AgentList[CEAgent]", network: "Network" ):
        for agent in agents:
            agent.update_tpb_subjective_norm_from_neighbors(agents, network)

    def agents_choice_after_cal(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.choice_after_calculation()

    def agent_diffusion_cal(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.diffusion_cal()

    def agent_Re_landfill_cal(self, recycleagents: "AgentList[Recycler]"):
        for agent in recycleagents:
            agent.landfill_cal()



    # def agents_attitude(self, agents: "AgentList[CEAgent]"):
    #     for agent in agents:
    #         agent.attitude_level_distribution()

    #第二课下1:06
    # buyer=agents.random_sample(1)[0]
    # seller = agents.random_sample(1)[0]
    # a = buyer.age+gruop