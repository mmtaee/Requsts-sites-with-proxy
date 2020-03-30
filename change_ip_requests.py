import requests, re, time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

def main(url):
    print("Getting proxy ip ...")
    req_proxy = RequestProxy()
    for ip_link in req_proxy.get_proxy_list() :
        ip = re.findall(r"(\d+.*)\|", str(ip_link))[0].strip()
        break
    proxies = {'http' : ip,}
    try :
        print ("requests to Url ...")
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            return True
        else:
            return None
    except :
        return False
      
if __name__ == '__main__':
    url = input ("Paste url here : ")
    if ("http://" or "https://") not in url :
        url = "http://" + url
    repeat = True
    while repeat :
        Main = main(url)
        if not Main :
            print ("Proxy not working, sleep 10 min ang get new porxy ip ...")
            time.sleep(600)
        else :
            print("Request is done, sleep an hour ...")
            time.sleep(3600)

        if Main is None :
            print(f"Server error : {Main}, sleep an hour and try again ...")
            time.sleep(3600)


