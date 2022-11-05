import sqlalchemy

from Melodie import DataFrameInfo
from Melodie.data_loader import MatrixInfo

simulator_scenarios = DataFrameInfo(
    df_name="simulator_scenarios",
    file_name="simulator_scenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "run_num": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "period_hours": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "grid_x_size": sqlalchemy.Integer(),
        "grid_y_size": sqlalchemy.Integer(),
        "initial_infected_percentage": sqlalchemy.Float(),
        "young_percentage": sqlalchemy.Float(),
        "network_type": sqlalchemy.String(),
        "network_param_k": sqlalchemy.Integer(),
        "network_param_p": sqlalchemy.Float(),
        "network_param_m": sqlalchemy.Integer(),
        "vaccination_trust_percentage": sqlalchemy.Float(),
        "vaccination_ad_percentage": sqlalchemy.Float(),
        "vaccination_ad_success_prob": sqlalchemy.Float(),
        "vaccination_neighbor_success_threshold": sqlalchemy.Float(),
        "vaccination_action_prob": sqlalchemy.Float(),
        "infection_prob": sqlalchemy.Float(),
        "reinfection_prob": sqlalchemy.Float(),
        "vaccinated_infection_prob": sqlalchemy.Float(),
    },
)

id_age_group = DataFrameInfo(
    df_name="id_age_group",
    file_name="id_age_group.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "age_group": sqlalchemy.String(),
        "prob_s1_s1": sqlalchemy.Float(),
        "prob_s1_s2": sqlalchemy.Float(),
        "prob_s1_s3": sqlalchemy.Float(),
        "move_radius": sqlalchemy.Integer(),
    },
)

id_health_state = DataFrameInfo(
    df_name="id_health_state",
    file_name="id_health_state.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "health_state": sqlalchemy.String()
    },
)

id_vaccination_trust = DataFrameInfo(
    df_name="id_vaccination_trust",
    file_name="id_vaccination_trust.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "vaccination_trust": sqlalchemy.String()
    },
)

agent_params = DataFrameInfo(
    df_name="agent_params",
    columns={
        "scenario_id": sqlalchemy.Integer(),
        "id": sqlalchemy.Integer(),
        "age_group": sqlalchemy.Integer(),
        "health_state": sqlalchemy.Integer(),
        "init_choice": sqlalchemy.Integer(),
    },
)

grid_stay_prob = MatrixInfo(
    mat_name="grid_stay_prob",
    data_type=sqlalchemy.Float(),
    file_name="grid_stay_prob.xlsx",
)

theory_plane_behaviour = DataFrameInfo(
    df_name="theory_plane_behaviour",
    file_name="theory_plane_behaviour.xlsx",
    columns={
        "att_distrib_param_eol_a": sqlalchemy.Float(),
        "att_distrib_param_eol_b": sqlalchemy.Float(),
        "id": sqlalchemy.Integer(),
        "wa": sqlalchemy.Float(),
        "wsn": sqlalchemy.Float(),
        "wpbc": sqlalchemy.Float(),
        "miu": sqlalchemy.Float(),
        "theita": sqlalchemy.Float(),
        "cost_repairing": sqlalchemy.Float(),
        "cost_reusing": sqlalchemy.Float(),
        "cost_recycling": sqlalchemy.Float(),
        "cost_landfill": sqlalchemy.Float(),
        "cost_storing": sqlalchemy.Float(),

    },
)

recycler_agent = DataFrameInfo(
    df_name="recycler_agent",
    file_name="recycler_agent.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "recycle_num": sqlalchemy.Integer(),
    },
)

recycle_params = DataFrameInfo(
    df_name="recycle_params",
    columns={
        "scenario_id": sqlalchemy.Integer(),
        "id": sqlalchemy.Integer(),
        "init_r_choice": sqlalchemy.Integer(),

    },
)