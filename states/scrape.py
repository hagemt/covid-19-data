#!/usr/bin/env python3
from bs4 import BeautifulSoup
from requests import get
import datetime, re, sys

# not sure if these CSS classes are actually constant...
FIND_DATE = 'SideNarrative_sidebar__1fizX' # has date (strong text)
FIND_ROWS = 'TFormat_main__35Moj' # has table w/ counts per state
#FIND_ROWS = 'TestingPositivity_tables-wrapper__2hAwr'

#JHU_URL = 'https://coronavirus.jhu.edu/testing/testing-positivity'
JHU_URL = 'https://coronavirus.jhu.edu/testing' # better for scrape:
JHU_URL = JHU_URL + '/states-comparison/testing-state-totals-bypop'
#USA_URL = 'https://hagemt.github.io/covid-19-data/usa' # Tor's maps

def fetch_soup(path=None, url=JHU_URL):
    now = datetime.datetime.utcnow() # different from date on rows (updated daily?)
    print('//GET %s (path=%s, when=%s)' % (url, path, now.isoformat()), file=sys.stderr)
    if path:
        try:
            with open(path, 'r') as f:
                return BeautifulSoup(f.read(), 'html.parser')
        except:
            print(sys.exc_info()[0], file=sys.stderr)

    prefix, suffix, = ('.jhu', re.sub(r'[^0-9]', '_', now.isoformat()))
    file_name = '%s.data.%s.html' % (prefix, suffix)
    response = get(url) # => 200 OK + HTML
    page_html = response.text
    try:
        with open(file_name, 'w') as f:
            f.write(page_html)
    except:
        print(sys.exc_info()[0], file=sys.stderr)
    return BeautifulSoup(page_html, 'html.parser')

def parse_soup(path=None, soup=None, url=JHU_URL):
    if soup is None: soup = fetch_soup(path=path, url=url)
    date = None # extracted from soup
    try:
        date = soup.find('div', class_=FIND_DATE).find('strong').text
    except:
        pass
    # per 100K persons, each state's % confirmed positives over total cases:
    fmt = lambda d: (d[0], 100 * float(d[2]) / float(d[1])) # d[3] is deaths

    data = soup.find('div', class_=FIND_ROWS).find_all('tr') # catch None?
    rows = (fmt([td.text for td in tr.find_all('td')]) for tr in data[1:])
    return (date, rows) # TODO: need to extract YYYY-MM-DD, format rows

def main():
    html_offline = None if len(sys.argv) < 2 else sys.argv[1]
    info, data = parse_soup(path=html_offline) # dated states
    sort = {'key': lambda columns: columns[1], 'reverse': True}
    for state_name, percent_positive, in sorted(data, **sort):
        print("['%s':%.2f]," % (state_name, percent_positive))
    print('//date on rows:', info, file=sys.stderr)

if __name__ == '__main__':
    main()
