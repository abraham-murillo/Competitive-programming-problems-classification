from pprint import pprint
import urllib3
import random
import requests
from pprint import pprint
from multiprocessing import Pool


# Due to timelimit of request the ip is usually banned temporaly, to fix that we need to use different ips for scrapping


def isValidProxy(proxy):
    url = "https://codeforces.com/problemset/problem/1783/G"
    try:
        r = requests.get(url, proxies={"http": proxy, "https": proxy})
    except:
        pass

    if r.status_code == 200:
        print(proxy)
        return proxy

    return None


def getValidProxies():
    with open("proxies.txt", "r") as f:
        proxies = f.read().split("\n")
    f.close()

    with Pool(processes=50) as pool:
        validProxies = pool.map(isValidProxy, proxies)


# if __name__ == "__main__":
#     # getValidProxies()


index = 0
proxies = [
    "145.40.121.73:3128",
    "51.158.154.173:3128",
    "49.212.143.246:6666",
    "82.99.194.30:3128",
    "49.0.2.242:8090",
    "5.9.94.91:3128",
    "195.154.114.49:8123",
    "45.8.179.242:1337",
    "45.8.179.241:1337",
    "129.213.95.20:80",
    "187.204.126.28:8081",
    "107.172.73.179:7890",
    "201.222.45.0:999",
    "45.8.179.247:1337",
    "20.121.184.238:80",
    "104.238.183.155:8888",
    "194.87.188.114:8000",
    "189.203.212.101:9812",
    "45.91.133.137:8080",
    "31.186.239.245:8080",
    "191.97.15.19:999",
    "190.90.79.106:999",
    "185.39.50.2:1337",
    "188.132.222.10:8080",
    "193.123.103.34:8080",
    "200.236.208.69:3129",
    "190.63.35.30:9812",
    "115.144.109.179:10000",
    "200.94.142.218:999",
    "179.49.144.210:3128",
    "83.143.101.132:1234",
    "200.25.254.193:54240",
    "45.174.87.18:999",
    "103.15.140.121:44759",
    "103.239.200.170:65535",
    "51.79.50.31:9300",
    "158.51.127.45:9130",
    "210.201.86.72:8080",
    "115.144.101.200:10000",
    "185.198.61.146:3128",
    "139.255.41.118:8080",
    "90.114.27.196:3128",
    "137.184.110.36:443",
    "61.9.34.145:65535",
    "103.152.232.109:3125",
    "69.75.140.157:8080",
    "45.238.12.4:3128",
    "20.112.234.186:3128",
    "95.154.76.20:3128",
    "128.199.67.35:80",
    "72.167.52.91:1234",
    "45.232.77.14:9292",
    "88.202.230.32:3897",
    "139.59.82.255:3128",
    "190.14.249.174:999",
    "183.88.56.204:8213",
    "180.183.128.121:8080",
    "124.120.142.11:8080",
    "103.147.246.84:8080",
    "67.73.184.178:8081",
    "43.245.219.106:8080",
    "105.243.162.34:8080",
]


def getSameIP(url):
    return requests.get(url)


def getDifferentIPS(url, tries=0):
    # Not that smart, but should work in most of cases
    global index

    if tries == len(proxies):
        print(f"I give up with {url}")
        return requests.get(url)

    proxy = proxies[index % len(proxies)]
    try:
        r = requests.get(url, proxies={"http": proxy, "https": proxy})
        return r
    except:
        index += 1
        return get(url, tries + 1)


# Try to make it work https://pypi.org/project/requests-ip-rotator/
# from requests_ip_rotator import ApiGateway, EXTRA_REGIONS
# gateway = None
# session = None

# aws_access_key_id = XXXXX
# aws_secret_access_key = XXXXX


# def start():
#     # Create gateway object and initialise in AWS
#     gateway = ApiGateway(
#         "https://site.com",
#         regions=EXTRA_REGIONS,
#         access_key_id=f"{aws_access_key_id}",
#         access_key_secret=f"{aws_secret_access_key}",
#     )
#     gateway.start()

#     # Assign gateway to session
#     session = requests.Session()
#     session.mount("https://site.com", gateway)


# def shutdown():
#     # Delete gateways
#     gateway.shutdown()


# def getRequestsIpRotate(url):
#     try:
#         # Send request (IP will be randomised)
#         r = session.get(url, stream=True)
#         file_request_succeed = r.ok
#         if file_request_succeed:
#             return r
#     except Exception as e:
#         print("Rotated IP failed (%s)" % str(e))
#         if proxy_rotation_mode == "AWS":
#             gateway.shutdown()



# ----------------------------------
# https://www.scraperapi.com/ API KEY
API_KEY = "2d1e7cf32106c5e5cec6915afc05f963"


# def getScraperApi(url):
#     payload = {"api_key": API_KEY, "url": url}

#     try:
#         r = requests.get("http://api.scraperapi.com", params=payload)
#         file_request_succeed = r.ok
#         if file_request_succeed:
#             return r
#     except Exception as e:
#         print("Rotated IP failed (%s)" % str(e))


def get(url):
    return getSameIP(url)
