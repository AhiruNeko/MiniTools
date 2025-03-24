import os
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
from selenium import webdriver
from PIL import Image
import io
import time


def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": url
    }

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, "html.parser")

    server_link = soup.find("a", class_="change current")
    if not server_link:
        print("Failed to find data-server link")

    data_server = server_link.get("data-server")
    if not data_server:
        print("Failed to extract data-server")

    download_path = "./downloads"

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    img_tags = soup.find_all("img")

    download_count = 0

    supported_formats = ["png", "webp", "jpg", "jpeg"]

    for img in img_tags:
        img_url = img.get("data-src") or img.get("src")
        if not img_url:
            continue

        img_url = urljoin(url, img_url)

        img_name = os.path.basename(img_url)

        img_name = re.sub(r"[?*,]", "_", img_name)

        img_extension = os.path.splitext(img_name)[1].lower().replace(".", "")
        if img_extension not in supported_formats:
            print(f"Skipped: {img_name} (unsupported format)")
            continue

        try:
            img_data = requests.get(img_url, headers=headers).content

            image = Image.open(io.BytesIO(img_data))

            if image.format.lower() == "webp":
                img_name = os.path.splitext(img_name)[0] + ".jpg"
                image = image.convert("RGB")

            image.save(f"downloads/{img_name}")
            download_count += 1
            print(f"Downloaded and converted: {img_name}")
        except Exception as e:
            print(f"Failed to download or convert {img_url}: {e}")

    canvas_tags = soup.find_all("canvas")
    for i, canvas in enumerate(canvas_tags):
        try:
            data_srcset = canvas.get("data-srcset")
            if not data_srcset:
                print(f"Skipped <canvas> {i}: No data-srcset attribute")
                continue

            canvas_url = urljoin(data_server, data_srcset)

            response = requests.head(canvas_url, headers=headers)
            if response.status_code != 200:
                print(f"Resource not found: {canvas_url}")
                continue

            response = requests.get(canvas_url, headers=headers)
            if response.status_code == 200:

                image = Image.open(io.BytesIO(response.content))

                if image.format.lower() == "webp":
                    image = image.convert("RGB")
                    img_name = f"canvas_{i}.jpg"
                else:
                    img_name = f"canvas_{i}.{image.format.lower()}"

                image.save(f"downloads/{img_name}")
                print(f"Downloaded <canvas> {i}: {canvas_url} (saved as {img_name})")
                download_count += 1
            else:
                print(f"Failed to download <canvas> {i}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Failed to process <canvas> {i}: {e}")

    print(f"Total images downloaded: {download_count}\n")
