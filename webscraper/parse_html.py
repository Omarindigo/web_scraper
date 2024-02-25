from bs4 import BeautifulSoup

def extract_image_urls(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all('img')
    image_urls = [img['src'] for img in images if 'src' in img.attrs]
    return image_urls

if __name__ == "__main__":
    image_urls = extract_image_urls("page.html")
    with open("image_urls.txt", "w") as f:
        for url in image_urls:
            f.write(url + "\n")
