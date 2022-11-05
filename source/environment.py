import random
from typing import TYPE_CHECKING

from Melodie import Environment, AgentList

from .grid import CovidGrid
from .scenario import CEScenario

if TYPE_CHECKING:
    from Melodie import AgentList
    from .agent import CEAgent
    from .recycler import Recycler


class CEEnvironment(Environment):
    scenario: CEScenario

    def setup(self):
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0
        self.total_waste_product=0

    def agents_move(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.move()

    @staticmethod
    def agents_infection(agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.infect_from_neighbors(agents)

    def agents_update_vaccination_trust(self, agents: "AgentList[CEAgent]", network: "Network"):
        for agent in agents:
            if random.uniform(0, 1) <= self.scenario.vaccination_ad_percentage:
                agent.update_vaccination_trust_from_ad()
            agent.update_vaccination_trust_from_neighbors(network, agents,)

    def agents_take_vaccination(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.take_vaccination()

    @staticmethod
    def agents_health_state_transition(agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.health_state_transition()


    def agents_product_waste(self, agents: "AgentList[CEAgent]"):
        for agent in agents:
            agent.update_wastproduct()


    def agents_total_product(self, agents: "AgentList[CEAgent]"):
        self.setup()#这个setup可写可不写的原因是evn里的def setup里已经ok了，其他的def里的set up不写就报错
        for agent in agents:
            agent.total_waste()

    def agents_total_pbc(self, agents: "AgentList[CEAgent]"):
        self.setup()
        for agent in agents:
            agent.tpb_subjective_norm()


    def agents_agent_neighbors_norms(self,agents: "AgentList[CEAgent]", network: "Network" ):
        self.setup()         #注意agentlist和network的位置
        for agent in agents:
            agent.update_tpb_subjective_norm_from_neighbors(agents, network)


    def calc_population_infection_state(self, agents: "AgentList[CEAgent]"):
        self.setup()
        for agent in agents:
            if agent.health_state == 0:
                self.s0 += 1
            elif agent.health_state == 1:
                self.s1 += 1
            elif agent.health_state == 2:
                self.s2 += 1
            elif agent.health_state == 3:
                self.s3 += 1
            else:
                self.s4 += 1

    def agents_choice_after_cal(self, agents: "AgentList[CEAgent]"):
        self.setup()
        for agent in agents:
            agent.choice_after_calculation()

    def agent_difusion_cal(self, agents: "AgentList[CEAgent]"):
        self.setup()
        for agent in agents:
            agent.difusion_cal()


    def agent_Re_landfill_cal(self, recycleagents: "AgentList[Recycler]"):

        for agent in recycleagents:
            agent.landfill_cal()



    # def agents_attitude(self, agents: "AgentList[CEAgent]"):
    #     self.setup()
    #     for agent in agents:
    #         agent.attitude_level_distribution()

    #第二课下1:06
    # buyer=agents.random_sample(1)[0]
    # seller = agents.random_sample(1)[0]
    # a = buyer.age+gruop