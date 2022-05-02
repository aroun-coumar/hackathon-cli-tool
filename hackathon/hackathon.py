
"""hackathon.

Usage:
  hackathon -h | --help
  hackathon --version
  hackathon -l | --list
  hackathon -s | --save  PATH

Options:
  -h, --help            Show this screen.
  --version             Show version.
  -l, --list            Print hackathon list
  -s, --save            Save to the given PATH
  PATH                  Location where you wanna save your hackathons list as excel
"""


import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from docopt import docopt
from tabulate import tabulate
from IPython.display import display
from xlsxwriter import Workbook

url1='https://mlh.io/seasons/2022/events'


def get_html(url):
    link = requests.get(url)
    if link.status_code == 200:
        return link
    else:
        raise Exception("Bad request")

def hackfinder():
    site=get_html(url1)
    with open('hack.html','w') as f:
        f.write(site.text)
    topic=[]
    date_of_event=[]
    location_of_event = []
    mode=[]
    event_link=[]    
    doc=BeautifulSoup(site.text,'html.parser')
    topics_titles_tags=doc.find_all('h3',{'class':'event-name'})
    len(topics_titles_tags)
    event_date_tag=doc.find_all('p',{'class':'event-date'})
    len(event_date_tag)
    (event_date_tag[5].text).strip()
    location_tag=doc.find_all('div',{'class':'event-location'})
    ((location_tag[0].text.strip()).replace("\n","")).replace(" ","")
    event_link_tags=doc.find_all('a',{'class':'event-link'},{'itemprop':'url'})
    len(event_link_tags)
    mode_tag=doc.find_all('div',{'class':'event-hybrid-notes'})
    for tag in topics_titles_tags:
        topic.append(tag.text)
    for tag in event_date_tag:
        date_of_event.append(tag.text.strip()) 
    for tag in location_tag:
        location_of_event.append(tag.text.replace("\n","").replace(" ",""))       
    for tag in mode_tag:
        mode.append(tag.text.replace("\n",""))
    for tag in event_link_tags:
        event_link.append(str(tag['href']))
    topics_dict={
    'Hackathon Name':topic,
    'Event date':date_of_event,
    'Event Location':location_of_event,
    'Event Mode':mode,
    'Even Link':event_link    
                }
    Hackathonsdf = pd.DataFrame(topics_dict) 
    return Hackathonsdf
                    
def main():
    args=docopt(__doc__,version='hackathon 1.0.11')
    util(args)


def util(docopt_args):   
    if docopt_args["--list"]:
        Hackathonsdf=hackfinder()
        print(tabulate(Hackathonsdf, headers='keys', tablefmt='psql'))

    
    elif docopt_args["--save"]:
        if os.path.isdir(docopt_args["PATH"]):
            Hackathonsdf=hackfinder()
            name_of_file = input("\nWhat is the name of the file: \n")
            file_path = os.path.join(docopt_args["PATH"] , name_of_file + ".xlsx")
            writer = pd.ExcelWriter(file_path , engine='xlsxwriter')
            Hackathonsdf.to_excel(writer, sheet_name='Sheet1')
            writer.save()

    else:
        print("Do it properly")    

if __name__=='__main__':
    main() 
    