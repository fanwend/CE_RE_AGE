from Melodie import Scenario


class CEScenario(Scenario):

    def setup(self):
        self.period_num = 0
        self.agent_num = 0
        self.recycle_num = 0  # 新agent类在这里也要生成
        self.network_type = ""
        self.network_param_k = 0
        self.network_param_p = 0
        self.network_param_m = 0

    def get_network_params(self):
        if self.network_type == "barabasi_albert_graph":
            network_params = {"m": int(self.network_param_m)}
        elif self.network_type == "watts_strogatz_graph":
            network_params = {"k": int(self.network_param_k), "p": int(self.network_param_p)}
        else:
            raise NotImplementedError
        return network_params

    #一、从theory_plane_behaviour中读取agent的预设参数
    #二、先把表弄到scenario里才能进一步的使用表中的信息，相应的，再使用对用表中的内容需要申明的内容就
    #较少了，参照本页中前两个函数，第二个函数申明的就省事了。是不是这样需要进一步查明。
    # def get_attitude_level_distribution_param(self):这块错了可能是需要在本部分的setup里执行一下，像self.setup_age_group_params()
    #     agent_personality = self.get_dataframe(data_info.theory_plane_behaviour)
    #     self.id0_ap_a = agent_personality.at[0, "att_distrib_param_eol_a"]
    #     self.id0_ap_b = agent_personality.at[0,"att_distrib_param_eol_b"]
    #     # self.id1_ap_a = agent_personality.at[0, "att_distrib_param_eol_a"]
    #     # self.id1_ap_b = agent_personality.at[0,"att_distrib_param_eol_b"]
    # def get_attitude_leve_para(self):
    #     # if id == 0:
    #     a = self.id0_ap_a
    #     b = self.id0_ap_b
    #     return (0-a)/b, (1-a), a, b
    #     # else:
    #     #     return (0-self.id1_ap_a)/self.id1_ap_b,(1-self.id1_ap_a), self.id1_ap_a, self.id1_ap_b