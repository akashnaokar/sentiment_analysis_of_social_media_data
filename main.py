from tqdm import tqdm
import os
import hydra
from hydra.core.config_store import ConfigStore
import pandas as pd
from src.utils import unzip_data
from src.data import preprocessing 
from src import configs

@hydra.main(version_base=None, config_path='configs/', config_name='config')
def main(cfg):
    # Extract the raw data
    unzip_data.unzip(cfg)

    # read, clean and store the data
    preprocessing.preprocessdata(cfg)




if __name__ == '__main__':
    main()