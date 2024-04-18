from dataclasses import dataclass


@dataclass
class Paths:
    root_dir: str
    data_dir : str
    log_dir : str

@dataclass
class Files:
    dataset: str

@dataclass
class NLPConfig:
    paths: Paths
    files: Files