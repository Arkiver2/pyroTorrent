#!/usr/bin/env python
"""
pyroTorrent module.
"""

from flup.server.fcgi import WSGIServer
from jinja2 import Environment, PackageLoader

from webtool import WebTool, read_post_data

import datetime
import time

# For unescaping
import urllib

# Regex
import re

from beaker.middleware import SessionMiddleware

import simplejson as json

from config import *

from sessionhack import SessionHack, SessionHackException

from model.rtorrent import RTorrent
from model.torrent import Torrent

def pyroTorrentApp(env, start_response):
    """
    pyroTorrent main function.
    """

    # Log here if you want

    r = wt.apply_rule('/torrent', env)
    #r = wt.apply_rule(env['REQUEST_URI'], env)
    # 404
    if r is None:
        start_response('404 Not Found', [('Content-Type', 'text/html')])

    elif type(r) in (tuple, list) and len(r) >= 1:
        # Respond with custom type.
        start_response('200 OK', [('Content-Type', r[0])])
        r = r[1]

    # 200
    else:
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])

    # Response data
    return [r]

def template_render(template, vars, default_page=True):
    """
        Template Render is a helper that initialisaes basic template variables
        and handles unicode encoding.
    """
    vars['base_url'] = BASE_URL

    # You can add more to vars here, such as a cached libTorrent version.
    if default_page:
        global libtorrentversion
        vars['libtorrentversion'] = libtorrentversion

    return unicode(template.render(vars)).encode('utf8')


# These *_page functions are what you would call ``controllers''.
def main_page(env):
    global global_rtorrent

    t = TorrentRequester('')

    t.get_name().get_download_rate().get_upload_rate() \
            .is_complete().get_size_bytes().get_download_total().get_hash()

    torrents = t.all()

    r = global_rtorrent.query().get_upload_rate().get_download_rate()

    rtorrent_data = r.first()

    tmpl = jinjaenv.get_template('download_list.html')

    return template_render(tmpl, {'session' : env['beaker.session'],
        'torrents' : t, 'rtorrent_data' : rtorrent_data} )

def torrent_info_page(env, torrent_hash):
    pass

if __name__ == '__main__':
    jinjaenv = Environment(loader=PackageLoader('pyrotorrent', 'templates'))
    jinjaenv.autoescape = True
    wt = WebTool()

    # Add all rules
    execfile('rules.py')

    # Global helpers
    global_rtorrent = RTorrent(**rtorrent_config)

    libtorrentversion = global_rtorrent.get_libtorrent_version()

    WSGIServer(SessionMiddleware(SessionHack(pyroTorrentApp), \
            session_options)).run()
