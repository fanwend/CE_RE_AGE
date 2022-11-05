from Melodie import Simulator
from config import config
from source.data_loader import CEDataLoader
from source.model import CEModel
from source.scenario import CEScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=CEModel,
        scenario_cls=CEScenario,
        data_loader_cls=CEDataLoader
    )
    simulator.run()
