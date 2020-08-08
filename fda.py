#!/usr/bin/env python3
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
import pandas as pd, sys, os

class Recipe:
    def __init__(self, *args, **kwargs):
        self.ingredients = args
        self.other_stuff = kwargs

def load_data(root_path, data_path='fda/recalls.csv'):
    csv_path = '%s/%s' % (root_path, data_path)
    data_frame = pd.read_csv(csv_path)
    data_frame['Date'] = data_frame['Date'].astype('datetime64')
    data_frame.set_index('Date', inplace=True)
    return data_frame

def ignore(product_type, recall_reason_description):
    pt_str = product_type.str # no recalls on drug or medical device
    not_food_if = pt_str.contains('Devices') | pt_str.contains('Drugs')
    return ~not_food_if & ~recall_reason_description.str.contains('ndecl')

def b_name_contains(brand_name, value):
    return value.str.contains(brand_name)

def p_name_contains(product_name, value):
    return value.str.contains(product_name)

def recall_contains(reason, value):
    return value.str.contains(reason)

def get_recalls(root_path):
    raw = load_data(root_path).fillna('') # DataFrame from CSV w/ '' = N/A
    filtered = raw[ignore(raw['Product Type'], raw['Recall Reason Description'])]

    print('-- recall reason matching ?cyclo:')
    cyclo = filtered[recall_contains('yclo', filtered['Recall Reason Description'])]
    print(cyclo)

    print('-- product description matching ?salad:')
    salad = filtered[p_name_contains('alad', filtered['Product Description'])]
    print(salad)

    print('-- in Meijer brand names:')
    meijers = filtered[b_name_contains('eijer', filtered['Brand Name(s)'])]
    print(meijers)

    print('-- most common company names:')
    bad_ten = filtered['Company Name'].value_counts()[:10]
    print(bad_ten)

    return None

def show_plots(data):
    plt.style.use('ggplot')
    #plt.subplots(figsize=(15,7))
    grouped = data.groupby([data.index.year, data.index.month])
    ax = grouped.count().plot(kind='bar')
    # X axis, major ticks every week in Month DD format:
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    #ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    #plt.plot(data.index, ax=ax)
    plt.show()

if __name__ == '__main__':
    USAGE = 'USAGE: %s [recalls] # no args = graph CSV'
    command = sys.argv[1] if len(sys.argv) > 1 else None
    if command == 'recalls': print(get_recalls(os.getcwd()))
    else: print(USAGE, sys.argv[0], file=sys.stderr)
    show_plots(load_data(os.getcwd()))
