from bs4 import BeautifulSoup
import requests
import pandas as pd
import time, os


def scraper(query, pageno):
    """
    :param query: search query for amazon
    :param pageno: no.of page numbers
    :return: search results and their price
    """
    headers = {
        'authority': 'www.amazon.in',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US;q=0.9,en;q=0.8',
    }
    url = f'https://www.amazon.in/s?k={query}&page={pageno}&qid=1605605092&ref=sr_pg_{pageno}'
    print(url)
    print('waiting for 10 sec')
    time.sleep(10.0)
    session = requests.Session()
    session.trust_env = False
    response = session.get(url,headers=headers)
    model_name = []
    price = []
    if response.status_code == 200:
        soup =BeautifulSoup(response.text, 'html.parser')
        intersted_fields = soup.find_all('div',class_ ="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28")

        print(f'intrested fields:{len(intersted_fields)} in page no {pageno}')
        for item in intersted_fields:
            print('extracting values....')
            lm = item.h2.span
            p = item.div.find('span', class_="a-price")

            if lm is not None:
                model_name.append(lm.text)
            else:
                model_name.append('unknown_product')

            if p is not None:
                price.append(p.text.split('₹')[1])
            else:
                price.append('unknown_price')
    else:
        print(f'response code: {response.status_code}')

    df = pd.DataFrame({'name':model_name, 'price':price})

    return df

if __name__ == '__main__':
    fn = 'output_data'
    query = 'apple'
    for i in range(1,21):
        print(f'Page number: {i}')
        scrapped_data = scraper(query=query,pageno=i)
        if len(scrapped_data) !=0:
            if os.path.exists(os.path.join('output_data',f'scrapped_data_{query}.csv')):
                scrapped_data.to_csv(os.path.join(fn,f'scrapped_data_{query}.csv'),mode='a',index=False,header=False)
            else:
                scrapped_data.to_csv(os.path.join(fn,f'scrapped_data_{query}.csv'),index=False)

        else:
            print('no entries...\n')




