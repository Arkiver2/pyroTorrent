# Place all your globals here

# ``Base'' URL for your HTTP website
BASE_URL = '/torrent'
# HTTP URL for the static files
STATIC_URL = BASE_URL + '/static'
USE_OWN_HTTPD = False

BACKGROUND_IMAGE = 'space1.png'

USE_AUTH = False

torrent_users = {
    'test' : {
        'targets' : [],
        'background-image' : 'cat.png',
        'password' : 'test'
    }
}

## Exemplary SCGI setup using unix socket
#rtorrent_config = {
#    'sheeva' : {
#        'scgi' : {
#            'unix-socket' : '/tmp/rtorrent.sock'
#        }
#    }
#}
#
## Exemplary SCGI setup using scgi over network
#rtorrent_config = {
#    'sheeva' : {
#        'scgi' : {
#            'host' : '192.168.1.70',
#            'port' : 80
#        }
#    }
#}

# Exemplary HTTP setup using remote XMLRPC server. (SCGI is handled by the HTTPD
# in this case)
rtorrent_config = {
    'sheeva' : {
        'http' : {
            'host' : '192.168.1.70',
            'port' : 80,
            'url'  : '/RPC2',
        }
    }
#    ,
#    'sheevareborn' : {
#        'http' : {
#            'host' : '42.42.42.42',
#            'port' : 80,
#            'url'  : '/RPC2',
#        }
#    }
}
