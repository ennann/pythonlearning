# First ever Spider program.
# Download contents from baidu.com

from urllib.request import urlopen
import requests


# Define your web url, and simulate a web browser by defining the Header.
url = "https://www.baidu.com"
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

# Check the HTTP response code.
response = requests.get(url)
print(f"The HTTP response is : {response.status_code}")

# Get results, and write into file.
results = urlopen(url)
print(results.read().decode('utf-8'))
# soup = BeautifulSoup(results, "html.parser")


with open("spider_results.html", mode="w") as f:
    f.write(results.read().decode('utf-8'))
    print("The results was already stored in the file.")
