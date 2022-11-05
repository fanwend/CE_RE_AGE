from typing import TYPE_CHECKING

from Melodie import NetworkAgent

if TYPE_CHECKING:
    from source.scenario import CEScenario


class CEAgent(NetworkAgent):
    scenario: "CEScenario"

    def set_category(self):
        self.category = 1

    def setup(self):
        self.init_choice = 0
        self.waste_product = 0
        self.total_wasteprod = 0
        self.attitude_level = 0.0
        self.knowledge_level = 0.0
        self.subjective_norm = 0.0
        self.decisions = ""
        self.total_wasteprod_difusion = 0.0
        self.agent_neighbors_norms = 0.0

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

    def update_tpb_subjective_norm_from_neighbors(self, agents, network):#注意agents和network的位置
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

    def diffusion_cal(self):
        '''
        字符串实验
        '''
        if self.decisions == "old":
            self.total_wasteprod_difusion = self.total_wasteprod-10
        else:
            self.total_wasteprod_difusion = self.total_wasteprod + 10
        return self.total_wasteprod_difusion