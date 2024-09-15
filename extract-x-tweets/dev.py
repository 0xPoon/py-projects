from bs4 import BeautifulSoup
import requests

# the html code which will go in the file GFG.html
# html = """
# <iframe src="https://sslecal2.investing.com?columns=exc_actual,exc_forecast,exc_previous&category=_inflation&importance=3&countries=5&calType=week&timeZone=8&lang=1" width="650" height="467" frameborder="0" allowtransparency="true" marginwidth="0" marginheight="0"></iframe><div class="poweredBy" style="font-family: Arial, Helvetica, sans-serif;"><span style="font-size: 11px;color: #333333;text-decoration: none;">Real Time Economic Calendar provided by <a href="https://www.investing.com/" rel="nofollow" target="_blank" style="font-size: 11px;color: #06529D; font-weight: bold;" class="underline_link">Investing.com</a>.</span></div>
# """

def get_data():
    url = 'https://www.investing.com/webmaster-tools/economic-calendar'

    response = requests.get(url)

    # set the proxies in the session object
    # 'https://sslecal2.investing.com?columns=exc_actual,exc_forecast,exc_previous&category=_inflation&importance=3&countries=5&calType=week&timeZone=8&lang=1'

    # print(html)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    test = open('test.html', 'w')
    test.write(response.text)
    test.close()

# print(soup.prettify())
get_data()
