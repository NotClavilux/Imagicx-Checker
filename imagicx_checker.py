import requests
import concurrent.futures
import random
import string
from tqdm import tqdm
import re

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_url():
    random_string = generate_random_string()
    return f"https://imagicx.de/i/{random_string}"

def is_url_valid(session, url, proxy):
    try:
        response = session.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        
        
        if 'The screenshot was deleted or not found' in response.text:
            return False
        else:
            return True
    except requests.RequestException:
        return False

def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

def check_url(args):
    url, proxy, session = args
    status = f"Checking URL: {url} using proxy: {proxy}"
    if is_url_valid(session, url, proxy):
        return status + " - Valid"
    else:
        return status + " - Invalid"

def main():
    num_urls = 1000  # change url number here
    proxy_file = 'proxies.txt'

    proxies = read_proxies_from_file(proxy_file)
    urls = [generate_random_url() for _ in range(num_urls)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        session = requests.Session()
        args_list = ((url, random.choice(proxies), session) for url in urls)
        results = list(tqdm(executor.map(check_url, args_list), total=num_urls))

    with open('hit.txt', 'w') as hit_file:
        url_pattern = re.compile(r'Checking URL: (.+) using proxy:')
        for result in results:
            print(result)
            match = url_pattern.search(result)
            if match and "Valid" in result:
                hit_file.write(match.group(1) + '\n')

if __name__ == "__main__":
    main()
