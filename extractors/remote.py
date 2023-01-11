from bs4 import BeautifulSoup
from requests import get

def extract_remote(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code != 200:
        print("Can't get jobs.")
    else:
        results=[]
        soup = BeautifulSoup(request.text, "html.parser")
        bodys = soup.find_all('td', class_="company position company_and_position")
        bodys.pop(0)
        for body in bodys:
            
            title = body.find('h2', itemprop="title")
            company = body.find('h3', itemprop="name")
            
            anchors = body.find_all('a', itemprop="url", class_="preventLink")
            for anchor in anchors:
                link = anchor['href']
            location_2 = body.find('div', class_="location")
            locations = body.find_all('div', class_="location")
            for location in locations:
                pay = location
            jobs_data={
                'company': company.string.strip().replace(","," "),
                'title': title.string.strip().replace(","," "),
                'location':location_2.string.strip().replace(","," "),
                'pay':pay.string.strip().replace(","," "),
                'link':f"https://remoteok.com/remote-jobs{link}"
            }
            results.append(jobs_data)
    return results
        
        
        
        
       
        
        
        
        
    
        