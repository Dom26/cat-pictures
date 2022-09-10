import requests
import shutil

def main():
    url = "https://cataas.com/c"
    filename = "fileImage.jpg"
    response = requests.get(f"{url}", stream=True)
    if response.status_code == 200:
        print("data fetched successfully")
        response.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(response.raw,f)
        
        print(f"image saved to {filename} successfully")
    else:
        print(f"There was a problem fetching the data. Code {response.status_code} was returned")

if __name__ == "__main__":
    main()