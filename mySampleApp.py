import re
import requests
import shutil
import sys
import argparse

def main(outFile,text):
    url = "https://cataas.com/c"
    filename = outFile
    if not text == None:
        url += f"/s/{text}"
    
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
    parser = argparse.ArgumentParser(description='Writes a random cat image to a given image file')
    parser.add_argument('-o',dest='outputFile',help='output file to be written to',required=True)
    parser.add_argument('-t',dest='text',help='Text to be included in output file')
    args = parser.parse_args()
    #print(args)
    #print(args.outputFile)
    #print(args.text)
    main(args.outputFile,args.text)