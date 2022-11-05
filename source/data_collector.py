from Melodie import DataCollector


class CovidDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property("agents", "waste_product")
        self.add_agent_property("agents", "total_wasteprod")
        self.add_agent_property("agents", "subjective_norm")  #“。。。”里面是agentReturn的数据
        self.add_agent_property("agents", "decisions")
        self.add_agent_property("agents", "total_wasteprod_difusion")
        self.add_agent_property("agents", "agent_neighbors_norms")
        self.add_agent_property("recycle_agents", "landfill_product")  # 在modle里设置的名字
        self.add_environment_property("total_waste_product")

