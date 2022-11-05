import random
from typing import TYPE_CHECKING

from Melodie import GridAgent, AgentList, Network

from .grid import CovidSpot

from scipy.stats import truncnorm

if TYPE_CHECKING:
    from .scenario import CEScenario


class CEAgent(GridAgent):
    scenario: "CEScenario"

    def set_category(self):#这部分跟grid有关，但是没学懂，在三上44min
        self.category = 0

    def setup(self):
        self.x = 0
        self.y = 0
        self.age_group = 0
        self.health_state = 0
        self.vaccination_trust_state = 0
        self.init_choice = 0
        self.waste_product = 0
        self.total_wasteprod = 0
        self.attitude_level = 0.
        self.knowledge_level = 0.
        self.subjective_norm = 0.
        self.decisions = ""
        self.total_wasteprod_difusion = 0.
        self.agent_neighbors_norms = 0.





    def move(self):
        spot: "CovidSpot" = self.grid.get_spot(self.x, self.y)
        stay_prob = spot.stay_prob
        if random.uniform(0, 1) < stay_prob:
            pass
        else:
            move_radius = self.scenario.get_move_radius(self.age_group)
            self.rand_move_agent(move_radius, move_radius)

    def infect_from_neighbors(self, agents: "AgentList[CEAgent]"):
        infection_prob = self.scenario.get_infection_prob(self.health_state)
        if infection_prob > 0:
            neighbors = self.grid.get_neighbors(self)
            for neighbor_category, neighbor_id in neighbors:
                neighbor_agent: "CEAgent" = agents.get_agent(neighbor_id)
                if (
                    neighbor_agent.health_state == 1
                    and random.uniform(0, 1) < infection_prob
                ):
                    self.health_state = 1
                    break

    def update_vaccination_trust_from_ad(self):
        if self.vaccination_trust_state == 0:
            if random.uniform(0, 1) <= self.scenario.vaccination_ad_success_prob:
                self.vaccination_trust_state = 1



    def update_vaccination_trust_from_neighbors(self, network, agents):
        if self.vaccination_trust_state == 0:
            neighbors = network.get_neighbors(self)
            neighbor_trust_count = 0
            for neighbor_category, neighbor_id in neighbors:
                neighbor_agent = agents.get_agent(neighbor_id)
                if neighbor_agent.vaccination_trust_state == 1:
                    neighbor_trust_count += 1
            if (
                neighbor_trust_count / len(neighbors)
                >= self.scenario.vaccination_neighbor_success_threshold
            ):
                self.vaccination_trust_state = 1



    def take_vaccination(self):
        if self.health_state == 0:
            if random.uniform(0, 1) <= self.scenario.vaccination_action_prob:
                self.health_state = 4

    def health_state_transition(self):
        if self.health_state == 1:
            (
                prob_s1_s1,
                prob_s1_s2,
                prob_s1_s3,
            ) = self.scenario.get_state_transition_prob(self.age_group)
            rand = random.uniform(0, 1)
            if rand < prob_s1_s1:
                pass
            elif prob_s1_s1 < rand < prob_s1_s1 + prob_s1_s2:
                self.health_state = 2
            else:
                self.health_state = 3


    def update_wastproduct(self):
        self.waste_product = 0 #name这行的意思是每个period用agent时都先变成零，因此需要累加的数不要放这行
        if self.init_choice == 0:
            self.waste_product = 1
        else:
            self.waste_product = 4
        return self.waste_product


    # 所有agent产生的废弃物的总和
    def total_waste(self):
        self.total_wasteprod =self.total_wasteprod + self.waste_product
        return self.total_wasteprod

    def tpb_subjective_norm(self):
        '''
        计划行为理论的应用,加权了知识和态度，来自于周围人的压力还没添加
        '''
        self.subjective_norm = self.attitude_level + self.knowledge_level
        return self.subjective_norm


    def update_tpb_subjective_norm_from_neighbors(self, agents,network):#注意agents和network的位置
        '''
        真正的计划行为理论的应用,规范来源于周边人的压力
        '''
        neighbors = network.get_neighbors(self)
        neighbor_norm = 0
        for neighbor_category,neighbor_id in neighbors:
            neighbor_agent = agents.get_agent(neighbor_id)
            if neighbor_agent.init_choice == 1:
                neighbor_norm += 1
        self.agent_neighbors_norms = neighbor_norm / len(neighbors)
        return self.agent_neighbors_norms



    def choice_after_calculation(self):
        '''
        根据态度进行的行为选择
        '''
        if self.subjective_norm > 9: #注意啊，return只有按这么写才认，两个return不认的，比如if一个return，else一个人return是不认的
            self.decisions = "old"
        else:
            self.decisions = "sell"
        return self.decisions

    def difusion_cal(self):
        '''
        字符串实验
        '''
        if self.decisions == "old":
            self.total_wasteprod_difusion = self.total_wasteprod-10
        else:
            self.total_wasteprod_difusion = self.total_wasteprod + 10
        return self.total_wasteprod_difusion