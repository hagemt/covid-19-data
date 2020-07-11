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

USAGES = 'USAGE: %s gif data_dir out_gif'
PREFIX = 'https://storage.googleapis.com/crc-assets/state-timeline/images'
IMAGES = PREFIX + '/downloads/state-timeline-%s-%s-event-0.png'

def data():
    '''Save 100x images into two data folders'''
    data_path = '%s/%s' % (os.getcwd(), 'data')
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

def gifs(data_path='data', gif_path='jhu.gif'):
    '''Make three .gif files: one in each of two variants + one combined'''
    print('-- generating GIFs...')
    gif_path_home = os.getcwd() # TODO: pass this?
    #gif_path_doom = '%s/new-death.%s' % (gif_path_home, gif_path)
    #gif_path_case = '%s/new-confirmed-cases.%s' % (gif_path_home, gif_path)
    gif_path_both = '%s/%s' % (gif_path_home, gif_path)
    with imageio.get_writer(gif_path_both, mode='I') as writer:
        for variant in ('new-confirmed-cases', 'new-deaths'):
            variant_path = '%s/%s' % (data_path, variant)
            for state in STATES:
                file_path = '%s/%s-%s.png' % (variant_path, state, variant)
                writer.append_data(imageio.imread(file_path))

if __name__ == '__main__':
    '''USAGE: no args = download JHU images; "$0 gif" turns data into GIFs'''
    program_name = sys.argv[0]
    has_args = len(sys.argv) > 1
    build_gifs = (sys.argv[1] == 'gif') if len(sys.argv) == 4 else False
    if build_gifs or not has_args: data()
    if build_gifs: gifs(data_path=sys.argv[2], gif_path=sys.argv[3])
    elif has_args: print(USAGES % (program_name))
