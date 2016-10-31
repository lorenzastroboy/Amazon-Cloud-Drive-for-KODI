'''
    Copyright (C) 2014-2016 ddurdle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''


from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

import re
import urllib, urllib2

import xbmc, xbmcaddon, xbmcgui, xbmcplugin


class MyHTTPServer(HTTPServer):

    def __init__(self, *args, **kw):
        HTTPServer.__init__(self, *args, **kw)
        self.ready = True

    def setDomain(self, service, domain):
        self.service = service
        self.domain = domain
        self.ready = True



class myStreamer(BaseHTTPRequestHandler):


    #Handler for the POST requests
    def do_HEAD(self):

        return

    #Handler for the POST requests
    def do_GET(self):

        if self.path == '/kill':
            self.server.ready = False

        else:
            url =  str(self.server.domain) + str(self.path)
            print url

            req = urllib2.Request(url,  None,  self.server.service.getHeadersList())
            try:
                response = urllib2.urlopen(req)
            except urllib2.URLError, e:
                if e.code == 403 or e.code == 401:
                    print "ERROR\n"
                    self.server.service.refreshToken()
                    req = urllib2.Request(url,  None,  self.server.service.getHeadersList())
                    try:
                        response = urllib2.urlopen(req)
                    except:
                        return
                else:
                    return

            self.wfile.write(response.read())

            #response_data = response.read()
            response.close()

            #        for r in re.finditer('redirect\=(.*)' ,
            #                     post_body, re.DOTALL):
            #          redirect = r.group(1)
            #          print "ib ib" + post_body
            #          print "\n\n" + redirect
            #          break
            return
