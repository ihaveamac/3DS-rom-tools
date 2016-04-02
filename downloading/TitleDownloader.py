#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# badly mangled version of cearp's updatecdn to download titles directly
# by a lazy codekitty
# and then edited even more by ihaveamac :p
# usage: python2 TitleDownloader.py titleid version
# example:  python2 TitleDownloader.py 000400DB00017102 10288
#
# this needs make_cdn_cia in the user's PATH
# build it from these sources: https://github.com/ihaveamac/ctr_toolkit/tree/master/make_cdn_cia

import csv
import os
import sys
import re
import binascii
from struct import unpack, pack
import urllib2
import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('title', action='store', help='Title ID')
parser.add_argument('version', action='store', help='version number')
arguments = parser.parse_args()

##########From https://stackoverflow.com/questions/5783517/downloading-progress-bar-urllib2-python
def chunk_report(bytes_so_far, chunk_size, total_size):
    percent = float(bytes_so_far) / total_size
    percent = round(percent*100, 2)
    sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
    if bytes_so_far >= total_size:
        sys.stdout.write('\n')

def chunk_read(response, outfname, chunk_size=2*1024*1024, report_hook=None):
    fh = open(outfname,'wb')
    total_size = response.info().getheader('Content-Length').strip()
    total_size = int(total_size)
    bytes_so_far = 0
    data = []
    while 1:
        if report_hook:
            report_hook(bytes_so_far, chunk_size, total_size)
        chunk = response.read(chunk_size)
        bytes_so_far += len(chunk)
        if not chunk:
             break
        fh.write(chunk)
    fh.close()
##########


print '***************************'
print '╦ ╦┌─┐┌┬┐┌─┐┌┬┐┌─┐╔═╗╔╦╗╔╗╔\n║ ║├─┘ ││├─┤ │ ├┤ ║   ║║║║║\n╚═╝┴  ─┴┘┴ ┴ ┴ └─┘╚═╝═╩╝╝╚╝'
print '***************************\n'
print 'UpdateCDN\n'

print '***** DON\'T WORRY about this message: "[!] Caution, Ticket and TMD Title Versions do not match"\n'

titleid = arguments.title
version = arguments.version

rawdir = titleid + "/" + version + '/raw'
ciadir = titleid + "/" + version + '/cia'

if not os.path.exists(rawdir):
    os.makedirs(rawdir)
if not os.path.exists(ciadir):
    os.makedirs(ciadir)

baseurl = 'http://nus.cdn.c.shop.nintendowifi.net/ccs/download/' + titleid

print baseurl + '/cetk'
cetk = urllib2.urlopen(baseurl + '/cetk')
print baseurl + '/tmd.' + version
tmd = urllib2.urlopen(baseurl + '/tmd.' + version)

tmd = tmd.read()
cetk = cetk.read()

open(rawdir + '/cetk','wb').write(cetk)
open(rawdir + '/tmd','wb').write(tmd)

# Download Contents
contentCount = unpack('>H', tmd[0x206:0x208])[0]
fSize = 16*1024
print 'Downloading ' + str(contentCount) + ' title content(s), please wait...'
for i in xrange(contentCount):
    cOffs = 0xB04+(0x30*i)
    cID = format(unpack('>I', tmd[cOffs:cOffs+4])[0], '08x')
    cIDX = format(unpack('>H', tmd[cOffs+4:cOffs+6])[0], '04x')
    outfname = rawdir + '/' + cID
    response = urllib2.urlopen(baseurl + '/' + cID)
    chunk_read(response, outfname, report_hook=chunk_report)
print 'Title download complete\n'

makecommand = ' ' + rawdir + ' ' + ciadir + "/" + titleid + '.cia'
print('make_cdn_cia' + makecommand)
os.system('make_cdn_cia' + makecommand)
print ''
