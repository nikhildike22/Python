import requests
import random

def jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)

    print("Success Status:", response.status_code)

    data = response.json()

    if data["success"] and "data" in data:
        all_data = data["data"]["data"]
        random_joke = random.choice(all_data)

        category = random_joke["categories"]
        content = random_joke["content"]
        return category , content
    else:
        raise Exception("Failed to fatch Api")

def main():
    try:
        category , content = jokes()
        print(f"Category:{category}")
        print(f"Joke:{content}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
         main()