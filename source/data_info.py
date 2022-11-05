import sqlalchemy

from Melodie import DataFrameInfo

simulator_scenarios = DataFrameInfo(
    df_name="simulator_scenarios",
    file_name="simulator_scenarios.xlsx",
    columns={
        "id": sqlalchemy.Integer(),
        "run_num": sqlalchemy.Integer(),
        "period_num": sqlalchemy.Integer(),
        "agent_num": sqlalchemy.Integer(),
        "recycle_num": sqlalchemy.Integer(),
        "network_type": sqlalchemy.String(),
        "network_param_k": sqlalchemy.Float(),
        "network_param_p": sqlalchemy.Float(),
        "network_param_m": sqlalchemy.Float()
    },
)

agent_params = DataFrameInfo(
    df_name="agent_params",
    columns={
        "scenario_id": sqlalchemy.Integer(),
        "id": sqlalchemy.Integer(),
        "init_choice": sqlalchemy.Integer(),
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





