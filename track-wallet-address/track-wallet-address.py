import requests as rq
from bs4 import BeautifulSoup
import csv


# response = rq.get('https://pro-api.solscan.io/v1.0/token/holders?tokenAddress=EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm&limit=10&offset=0', auth=('<KEY>', '<KEY>'))
# URL =
# response = rq.get('https://solscan.io/token/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm#holders')

sess = rq.Session()

soup = BeautifulSoup(sess.get('https://solscan.io/token/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm#holders').text, 'html.parser')

# url = 'https://solscan.io/token/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm#holders'

print(soup.find_all('table', class_='[&_tr:last-child]'))
# , class_='[&_tr:last-child]:border-0'
# soup.find_all('p', id='id_name')

# ,  id='radix-:r6g:-content-holders'


#
#
# # print(soup)
# # =====================================
# #   CLASS TO PARSE HTML INPUT DATA
# # =====================================
# class Parse_HTML:
#
#     # ===========================================================
#     #  LOAD HTML DATA AND WRITE FILE PATH WHILE OBJECT CREATION
#     # ===========================================================
#     def __init__(self, html_data, write_file_path):
#         self._html_data = html_data
#         self._write_file_path = write_file_path
#
#     # =============================================
#     #   PARSER TO CONVERT HTML DATA TO DICTIONARY
#     # =============================================
#     def parser(self):
#         soup = BeautifulSoup(sess.get(url).text, "html.parser")
#         parser_dict = {}
#         for table in soup.findAll("table"):
#             for tr in table.findAll("tr"):
#                 parser_dict[tr.find("th").text.replace("\n", '')] = tr.find("td").text.replace("\n", '')
#         return parser_dict
#
#     # ===============================================
#     #  WRITE PARSED DATA (DICTIONARY) TO A CSV FILE
#     # ===============================================
#     def write_csv(self, data):
#         with open(self._write_file_path, 'w') as csvfile:
#             data_writer = csv.DictWriter(csvfile, fieldnames=list(data.keys()), lineterminator='\n')
#             data_writer.writeheader()
#             data_writer.writerows([data])
#             return True
#
#
# # =================================
# #  PROGRAM EXECUTION STARTS HERE
# # =================================
# ph = Parse_HTML(html_data=url, write_file_path='C:/Users/chris/Documents/py-projects/track-wallet-address/data/parsed_html_results.csv')
# parser_dict = ph.parser()
# confirm = ph.write_csv(data=parser_dict)
# if confirm is True:
#     print('File Created')
# else:
#     print('Not Able to Create a File')