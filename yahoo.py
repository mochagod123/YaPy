from bs4 import BeautifulSoup
import aiohttp

async def GetShopPage(商品名: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&p={商品名}&x=0&y=0") as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            return soup

async def GetName(ページ: str):
    try:
        
        base = ページ.find_all('a', {'class', "Product__titleLink js-browseHistory-add js-rapid-override"})[0]
        return base.get_text()

    except:
        return None
        
async def GetMoney(ページ: str):
    try:

        neda = ページ.find_all('span', {"class", "Product__priceValue u-textRed"})[0]
        return neda.get_text()

    except:
        return None

async def GetImageURL(ページ: str):
    try:

        img = ページ.find_all('img', {"class", "Product__imageData"})[0]
        return img["src"]

    except:
        return None

async def GetURL(ページ: str):
    try:

        base = ページ.find_all('a', {'class', "Product__titleLink js-browseHistory-add js-rapid-override"})[0]
        return base["href"]

    except:
        return None
    
async def GetTimeLimit(ページ: str):
    try:

        base = ページ.find_all('dd', {'class', "Product__time"})[0]
        return base.get_text()

    except:
        return None