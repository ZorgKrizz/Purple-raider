import requests
session = requests.Session()

def set_cookies():
    url = "https://discord.com/"

    headers = {
        "Authorization": "MTE2MjY5NDYxODc5MDUxNDc3OA.GwiOG5.yzCnAY99ALYtxT8dSt9N8kYo2XxGhVNFZ29V5M"
    }

    r = session.get(url, headers=headers)

    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)

headers = {
    "Accept": "*/*",
    #"Cookie": "dcfduid=9ae57cf06b2f11eeb1f91990c3189846; __sdcfduid=9ae57cf16b2f11eeb1f91990c3189846627cbb03f8071c0b579bf1e287022de7c0b941467df32721569253ce246e6bac; cf_clearance=yxZh8qJhU1FXfol7son7pSyxSAnqUCoiPfDYcvzO87E-1697362646-0-1-dcf3d73d.43ba70cd.628d79c7-0.2.1697362646; _gcl_au=1.1.616580489.1697362647; _ga=GA1.1.85325183.1697362647; __cfruid=26a47aa134333933fb64a890b9010f72fdd2cdb9-1697609881; _cfuvid=41nHs0WjZYQ2gRJNtTK_NdbemeimIvDxftFYGmRLV5s-1697609881689-0-604800000; OptanonConsent=isIABGlobal=false&datestamp=Wed+Oct+18+2023+06%3A18%3A02+GMT%2B0000+(Coordinated+Universal+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; locale=en-US; _ga_Q149DFWHT7=GS1.1.1697609882.3.0.1697609892.0.0.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "MTE2MjY5NDYxODc5MDUxNDc3OA.GwiOG5.yzCnAY99ALYtxT8dSt9N8kYo2XxGhVNFZ29V5M",
    "Content-Length": "49",
    "Content-Type": "application/json",
    "Origin": "https://discord.com",
    "Referer": "https://discord.com/channels/@me/1163056612202786907",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Linux",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Context-Properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6bnVsbCwibG9jYXRpb25fY2hhbm5lbF9pZCI6IjExNjMwNTY2MTIyMDI3ODY5MDciLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjEsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiIxMTY0MDg1MTI2ODAwNjE3NTUzIn0=",
    "X-Debug-Options": "bugReporterEnabled",
    "X-Discord-Locale": "en-US",
    "X-Discord-Timezone": "UTC",
    "X-Super-Properties": "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE4LjAuMC4wIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMzgxMTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
}

payload = {
    "session_id": "594d8df69250df37d644ee23a0c3d564"
}
set_cookies()

resp = session.post("https://discord.com/api/v9/invites/fortnite", headers=headers, json=payload)
print(resp.status_code)