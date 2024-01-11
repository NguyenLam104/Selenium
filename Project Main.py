from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urlparse, urljoin

def check_Error(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        all_links = driver.find_elements(By.TAG_NAME, 'a')

        for link in all_links:
            link_url = link.get_attribute('href')
            try:
                if not link_url:
                    print(f'Lỗi : Đường link không hợp lệ - {link_url}')
                    continue

                if urlparse(link_url).scheme == '':
                    link_url = urljoin(url, link_url)

                try:
                    response = requests.get(link_url)
                    response.raise_for_status()

                    if not response.text.strip():
                        print(f'Lỗi: Trang web trống - {link_url}')

                except requests.exceptions.RequestException as re:
                    print(f'Lỗi khi kiểm tra link {link_url}: {re}')
                    continue

                if response.status_code != 200:
                    print(f'Lỗi {response.status_code} - {link_url}')
            except Exception as e:
                print(f'Có lỗi xảy ra: {e}')

    finally:
        driver.quit()

check_Error("https://fit.dntu.edu.vn/")