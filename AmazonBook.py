import requests
from bs4 import BeautifulSoup
# from .url import url

url = "https://www.audible.com/adblbestsellers?searchCategory=18572029011&ref_pageloadid=36aExuQweCqum9Pv&ref=a_adblbests_l1_catRefs_3&pf_rd_p=2ea8d46b-3372-49db-8ad4-77416e49695f&pf_rd_r=MH73Y1CCKXC99GQAHXR0&pageLoadId=k5HSAj2iqAAhz7tN&creativeId=00b943e2-39f7-4416-aa6b-3c2695ade879"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

zg = soup.find_all("div", class_="adbl-page desktop")[0]
print(zg.prettify())