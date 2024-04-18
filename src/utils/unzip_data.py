from zipfile import ZipFile
from tqdm import tqdm
import os
import hydra

def unzip(cfg):

    data_dir = cfg.paths.data_dir
    dataset_name = cfg.files.dataset_name
    raw_data_dir= cfg.paths.raw_data_dir

    if not os.listdir(raw_data_dir):
        with ZipFile(os.path.join(data_dir, dataset_name), 'r') as archive:
            for file in tqdm(iterable=archive.namelist(), total=len(archive.namelist())):
                archive.extract(path = raw_data_dir, member = file)

    else:
        print('Data already extracted. Skipping extraction process.')

if __name__ == "__main__":
    unzip()

