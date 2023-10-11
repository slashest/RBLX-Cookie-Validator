import requests

def check_cookie(cookie: str) -> str:
    response = requests.get("https://www.roblox.com/home", cookies={".ROBLOSECURITY": token})
    if "data-name" in response.text:
        print("Valid cookie")
    else:
        print("Invalid cookie")

def main():
    try:
        while True:
            token = input("Cookie: ").strip()
            check_cookie(cookie)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
