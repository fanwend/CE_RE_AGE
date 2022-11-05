from typing import TYPE_CHECKING

import numpy as np
from Melodie import DataLoader

from source import data_info

from scipy.stats import truncnorm

if TYPE_CHECKING:
    from .scenario import CEScenario


class CEDataLoader(DataLoader):
    def setup(self):
        self.load_dataframe(data_info.simulator_scenarios)
        self.load_dataframe(data_info.id_age_group)
        self.load_dataframe(data_info.id_health_state)
        self.load_dataframe(data_info.id_vaccination_trust)
        self.load_dataframe(data_info.recycler_agent) ##在info里注册了这里得setup
        self.load_matrix(data_info.grid_stay_prob)
        self.load_dataframe(data_info.theory_plane_behaviour)
        self.generate_agent_dataframe()
        self.generate_recycle_dataframe()  # generate_recycle要这里创建一下

    @staticmethod
    def init_age_group(scenario: 'CEScenario'):
        young_percentage = scenario.young_percentage
        age_group = 0
        if np.random.uniform(0, 1) > young_percentage:
            age_group = 1
        return age_group

    @staticmethod
    def init_health_state(scenario: 'CEScenario'):
        infection_percentage = scenario.initial_infected_percentage
        health_state = 0
        if np.random.uniform(0, 1) < infection_percentage:
            health_state = 1
        return health_state

    @staticmethod
    def init_vaccination_trust_state(scenario: 'CEScenario'):
        vaccination_trust_percentage = scenario.vaccination_trust_percentage
        vaccination_trust_state = 0
        if np.random.uniform(0, 1) < vaccination_trust_percentage:
            vaccination_trust_state = 1
        return vaccination_trust_state

    @staticmethod
    def my_init_choice(scenario: 'CEScenario'):
        in_choice = 0.5
        init_choice = 0
        if np.random.uniform(0, 1) < in_choice:
            init_choice = 1
        return init_choice

    @staticmethod
    def agent_attitude_level(scenario: 'CEScenario'):
        '''
        abcd根据文献生成了agent的自身的态度
        '''
        a = 1
        b = 2
        loc = 3
        scale = 4
        distribution = truncnorm(a, b, loc, scale)
        attitude_level = float(distribution.rvs(1))
        return attitude_level

    @staticmethod
    def extended_tpb_knowledge(scenario: 'CEScenario'):
        """
        agent的end-of-life 管理知识
        """
        loc = 1
        scale = 2
        distribution = truncnorm((0 - loc) / scale, (1 - loc) / scale,
                                 loc, scale)
        knowledge_level = float(distribution.rvs(1))
        return knowledge_level

    def generate_agent_dataframe(self):
        with self.dataframe_generator(
                data_info.agent_params,
                lambda scenario: scenario.agent_num
        ) as g:
            def generator_func(scenario: "CEScenario"):
                return {
                    "id": g.increment(),
                    "age_group": self.init_age_group(scenario),
                    "health_state": self.init_health_state(scenario),
                    "vaccination_trust_state": self.init_vaccination_trust_state(scenario),
                    "init_choice": self.my_init_choice(scenario),
                    "attitude_level": self.agent_attitude_level(scenario),
                    "knowledge_level": self.extended_tpb_knowledge(scenario),

                }

            g.set_row_generator(generator_func)


    @staticmethod
    def my_init_r_choice(scenario: 'CEScenario'):
        ini_choice = 0.5
        init_r_choice = 0
        if np.random.uniform(0, 1) < ini_choice:
            init_r_choice = 1
        return init_r_choice

    def generate_recycle_dataframe(self):
        with self.dataframe_generator(
                data_info.recycle_params,
                lambda scenario: scenario.recycle_num
        ) as g:
            def generator_func(scenario: "CEScenario"):
                return {

                    "id": g.increment(),
                    "init_r_choice": self.my_init_r_choice(scenario),
                }

            g.set_row_generator(generator_func)
