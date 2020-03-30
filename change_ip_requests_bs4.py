import requests, time
from bs4 import BeautifulSoup

# a program to send requests many times to a server with proxy ip
def main(url):
        print("Getting proxy ip ")
        proxy_site_url = "https://free-proxy-list.net/"
        request_proxy_ip = requests.get(proxy_site_url)
        soup = BeautifulSoup (request_proxy_ip.text, "html.parser")
        get_ip = soup.select("tbody tr")
        proxy_list = []
        for i in range (14):
            https = get_ip[i].find("td", class_="hx").text
            if https == "yes" :
                ip_infos = get_ip[i].find_all("td", class_=None)
                ip = ip_infos[0].text
                port = ip_infos[1].text
                proxy = ip + ":" + port
                proxy_list.append(proxy)
        if len (proxy_list) == 0 :
                return None
        for ip in proxy_list :
                proxies = {'https' : ip.strip()}
                print (f"requests to Url with ip {ip} ")
                try :
                    response = requests.get(url, proxies=proxies)
                    if response.status_code == 200:
                        print (f"Request Sending Completed for ip : {ip}")
                        return True
                    else :
                        print (f"Error {response.status_code}")
                except : 
                     print("Try new proxy ip after sleep 1 min ")
                     time.sleep(60)
        return False       
      
if __name__ == '__main__':
    url = input ("Paste url here : ")
    while "http" not in url :
        url = input ("Paste url here with http : ")
    while True :
        Main = main(url)
        if Main is None :
            print ("No proxy ip for https . sleep 10 min and get new proxy ip list ")
            time.sleep(600)
        if not Main :
            print ("Proxy not working, sleep 10 min ang get new porxy ip list ")
            time.sleep(600)
        else :
            print("Request is done, sleep an hour ")
            time.sleep(3600)


