from kaggle.api.kaggle_api_extended import KaggleApi
import os


def getUpperDir(current_dir: str):
    path = current_dir.split("\\")
    return "\\".join(path)


def download_dataset(dataset: str, file_name: str) -> None:
    current_dir = os.getcwd()
    top_dir = getUpperDir(current_dir)
    data_dir = os.path.join(top_dir, ".data")
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset,
                               path=data_dir,
                               unzip=True
                               )


if __name__ == "__main__":
    download_dataset("mlg-ulb/creditcardfraud", "creditcard.csv")
