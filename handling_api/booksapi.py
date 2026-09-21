import requests
import random

def book_api():
    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        all_data = data["data"]["data"]
        random_book = random.choice(all_data)
        volume_info = random_book["volumeInfo"]

        authors =volume_info.get("authors", ["Unknown"])[0]
        # description = volume_info.get(
        #     "description",
        #       "No description available"
        # )
        categories = volume_info.get("categories", ["Unknown"])[0]
        imageLinks = volume_info.get("imageLinks", {}).get(
              "smallThumbnail",
                 "No image available"
        )

        return authors,categories,imageLinks
    else:
        raise Exception("failed to fatch api")

def main():
    try:
        authors,categories,imageLinks = book_api()
        print(f"Authors:={authors}")
        print(f"Categories:={categories}")
        # print(f"Description:={description}")
        print(f"ImageLinks:={imageLinks}")

    except Exception as e:
            print(e)

if __name__ == "__main__":
         main()
