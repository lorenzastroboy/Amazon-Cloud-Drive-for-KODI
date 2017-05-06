'''
    Amazon Cloud Drive for KODI / XBMC Plugin
    
    Copyright (C) 2013-2015 ddurdle
    
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

from urllib2 import HTTPRedirectHandler
from urllib2 import Request

class RedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if code in (301, 302, 303, 307):
            #If we are going to Amazon S3 we want to drop the Authorization header
            if 's3.amazonaws.com' in newurl:
                newheaders = dict((k,v) for k,v in req.headers.items()
                              if k.lower() not in ("authorization"))
            return Request(newurl, headers=newheaders)
        else:
            raise urllib2.HTTPError(req.get_full_url(), code, msg, headers, fp)
            
