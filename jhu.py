#!/usr/bin/env python3
import os, shutil, sys
import imageio, requests

STATES = (
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

USAGES = 'USAGE: %s data <out_gif>'
PREFIX = 'https://storage.googleapis.com/crc-assets/state-timeline/images'
IMAGES = PREFIX + '/downloads/state-timeline-%s-%s-event-0.png'

def data(data_dir='data', root_path='.'):
    '''Save 100x images into two data folders'''
    data_path = '%s/%s' % (root_path, data_dir)
    for variant in ('new-confirmed-cases', 'new-deaths'):
        variant_path = '%s/%s' % (data_path, variant)
        os.makedirs(variant_path, exist_ok=True)
        for state in STATES:
            file_path = '%s/%s-%s.png' % (variant_path, state, variant)
            r = requests.get(IMAGES % (variant, state), stream=True)
            with open(file_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print(file_path)

def gifs(data_dir='data', root_path='.', out_gif='out.gif'):
    '''Make three .gif files: one in each of two variants + one combined'''
    print('-- generating JHU GIF(s)...')
    gif_path = '%s/%s' % (root_path, out_gif)
    with imageio.get_writer(gif_path, mode='I') as gif:
        print(gif_path)
        data_path = '%s/%s' % (root_path, data_dir)
        for variant in ('new-confirmed-cases', 'new-deaths'):
            variant_path = '%s/%s' % (data_path, variant)
            for state in STATES:
                file_path = '%s/%s-%s.png' % (variant_path, state, variant)
                gif.append_data(imageio.imread(file_path))
                print(file_path)

if __name__ == '__main__':
    '''USAGE: no args = download JHU images; "$0 gif" turns data into GIFs'''
    out_gif = None if len(sys.argv) < 3 else sys.argv[2] # optional
    data_dir = 'data' if len(sys.argv) < 2 else sys.argv[1]
    root_path = os.getcwd() # FIXME: build paths properly
    error_bad = False # XXX: detect valid images, etc.
    warn_bad = False # TODO: detect root overwrite
    if error_bad or warn_bad:
        print(USAGES % (sys.argv[0]))
        if warn_bad: print('ERROR: %s (bad directory) or %s (data overwrite)'
                           % (data_path, file_out))
        sys.exit(1)
    if not os.path.exists(data_dir):
        data(data_dir=data_dir, root_path=root_path)
    if out_gif:
        gifs(data_dir=data_dir, root_path=root_path, out_gif=out_gif)
