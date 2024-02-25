import requests
import time
import os

def download_images(image_urls_file, save_folder="downloaded_images"):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(image_urls_file, 'r') as f:
        image_urls = f.read().splitlines()

    for i, url in enumerate(image_urls):
        try:
            print(f"Downloading {url}...")
            response = requests.get(url)
            if response.status_code == 200:
                file_path = os.path.join(save_folder, f'image_{i}.jpg')
                with open(file_path, 'wb') as file:
                    file.write(response.content)
            time.sleep(1)  # Rate limiting to avoid overwhelming the server
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    download_images("image_urls.txt")
