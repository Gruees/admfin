import requests
from termcolor import colored
import os

baner="""
                                             
  ,---.     ,--.           ,---.,--.         
 /  O  \  ,-|  |,--,--,--./  .-'`--',--,--,  
|  .-.  |' .-. ||        ||  `-,,--.|      \ 
|  | |  |\ `-' ||  |  |  ||  .-'|  ||  ||  | 
`--' `--' `---' `--`--`--'`--'  `--'`--''--' 
                                             
        Instagram:fernando_dors_
        Github:https://github.com/ZxNando/
"""
print(colored(baner,'green'))

link=str(input(colored('link: ','yellow')))
list_page=open('page.txt','r')
page_list=list_page.readlines()
list_page.close()

for page in page_list:
  admin=page.strip()
  adminn='/'+admin
  URL=link+adminn
  
  x=requests.get(URL)
  if x.status_code == 200:
    print(colored('Found: '+URL,'green'))
    break
  else:
    print(colored('Not found: '+URL,'red'))
    
  
  
