# -*- coding: utf-8 -*

from typing import Dict

from yacs.config import CfgNode

from .tracker import builder as tracker_builder
from .tracker.tracker_base import TRACK_PIPELINES

# from .segmenter import builder as segmenter_builder


def build_pipeline(task: str, cfg: CfgNode, **kwargs):
    """
    Build pipeline with specified task name & config
    :param task: specified task name
    :param cfg: CfgNode
    :param kwargs:
    :return:
    """
    if task == "track":
        track_pipeline = tracker_builder.build(cfg, **kwargs)
        return track_pipeline
    else:
        print("model for task {} is not complted".format(task))
        exit(-1)


def get_config() -> Dict[str, CfgNode]:
    """
    Get pipeline list config
    :return:
    """
    cfg_dict = {"track": CfgNode()}

    for cfg_name, module in zip([
            "track",
    ], [
            TRACK_PIPELINES,
    ]):
        cfg = cfg_dict[cfg_name]
        cfg["name"] = "unknown"
        for name in module:
            cfg[name] = CfgNode()
            tester = module[name]
            hps = tester.default_hyper_params
            for hp_name in hps:
                cfg[name][hp_name] = hps[hp_name]
    return cfg_dict
