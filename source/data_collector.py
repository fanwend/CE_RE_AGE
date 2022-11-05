from Melodie import DataCollector


class CovidDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property("agents", "health_state")
        self.add_agent_property("agents", "x")
        self.add_agent_property("agents", "y")
        self.add_agent_property("agents", "waste_product")
        self.add_agent_property("agents", "total_wasteprod")
        self.add_agent_property("agents", "subjective_norm")#“。。。”里面是agent   Return的数据
        self.add_agent_property("agents", "decisions")
        self.add_agent_property("agents", "total_wasteprod_difusion")
        self.add_agent_property("agents", "agent_neighbors_norms")
        self.add_agent_property("recycleagents", "landfill_product")#在modle里设置的名字
        self.add_environment_property("s0")
        self.add_environment_property("s1")
        self.add_environment_property("s2")
        self.add_environment_property("s3")
        self.add_environment_property("s4")
        self.add_environment_property("total_waste_product")

