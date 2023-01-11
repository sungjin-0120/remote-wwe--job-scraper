from requests import get
from bs4 import BeautifulSoup

def extractor_plannet(word):
    results=[]
    url= f"https://www.jobplanet.co.kr/search?query={word}"
    response = get(url)

    soup=BeautifulSoup(response.text,"html.parser")
    units = soup.find_all('div', class_="result_unit")
    for unit in units:
        cons = unit.find_all('div', class_="result_unit_con")
        for con in cons:
            infos = con.find_all('div', class_="result_unit_info")

            for info in infos:
                links = info.find('div', class_="unit_head")
                link = links.find('a', class_="posting_name")
                site=link["href"]
                name = info.find('p', class_="company_name")
                company = name.find('a', class_="btn_open")

                uis = info.find_all('div', class_="ui_fold_comp closed")
                for ui in uis:
                    tags = ui.find_all('span', class_="tags")
                    if len(tags) == 3:
                        region = tags[0]
                        occupation = tags[1]
                        exp = tags[2]
                        plan = {
                            'company':company.string,
                            'region':region.string,
                            'occupation':occupation.string,
                            'exp':exp.string,
                            'link': f"https://www.jobplanet.co.kr/{site}"
                        }
                        results.append(plan)

                    else:
                        region = tags[0]
                        occupation = tags[1]
                        size = tags[2]
                        exp = tags[3]
                        plan = {
                            'company':company.string,
                            'region':region.string,
                            'occupation':occupation.string,
                            'size':size.string,
                            'exp':exp.string,
                            'link': f"https://www.jobplanet.co.kr/{site}"
                            }
                        results.append(plan)
    return results

ki =extractor_plannet('java')
print(len(ki))