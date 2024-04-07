from zipfile import ZipFile
from tqdm import tqdm
import os
import hydra

@hydra.main(version_base=None, config_path='../../configs/', config_name='config')
def unzip(cfg):
    data_dir = cfg.paths.data_dir
    dataset_name = cfg.files.dataset_name

    with ZipFile(os.path.join(data_dir, dataset_name), 'r') as archive:
        for file in tqdm(iterable=archive.namelist(), total=len(archive.namelist())):
            archive.extract(path = data_dir, member = file)

if __name__ == "__main__":
    unzip()

