#!/usr/bin/env python3
import os, shutil
import requests

prefix = 'https://storage.googleapis.com/crc-assets/state-timeline/images'
images = prefix + '/downloads/state-timeline-%s-%s-event-0.png'

states = (
'alabama',
'alaska',
'arizona',
'arkansas',
'california',
'colorado',
'connecticut',
'delaware',
'florida',
'georgia',
'hawaii',
'idaho',
'illinois',
'indiana',
'iowa',
'kansas',
'kentucky',
'louisiana',
'maine',
'maryland',
'massachusetts',
'michigan',
'minnesota',
'mississippi',
'missouri',
'montana',
'nebraska',
'nevada',
'new-hampshire',
'new-jersey',
'new-mexico',
'new-york',
'north-carolina',
'north-dakota',
'ohio',
'oklahoma',
'oregon',
'pennsylvania',
'rhode-island',
'south-carolina',
'south-dakota',
'tennessee',
'texas',
'utah',
'vermont',
'virginia',
'washington',
'west-virginia',
'wisconsin',
'wyoming',
)

def main():
    '''Save 100x images into two data folders'''
    data_path = '%s/%s' % (os.getcwd(), 'data')
    for variant in ('new-confirmed-cases', 'new-deaths'):
        variant_path = '%s/%s' % (data_path, variant)
        os.makedirs(variant_path, exist_ok=True)
        for state in states:
            file_path = '%s/%s-%s.png' % (variant_path, state, variant)
            r = requests.get(images % (variant, state), stream=True)
            with open(file_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print(file_path)

if __name__ == '__main__':
    main()
