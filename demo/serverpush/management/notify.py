import logging
import json

import eventlet

class HookboxNotify(object):
	logger = logging.getLogger('hookbox')
	
	def __init__(self, callback):
		self.event = callback
		
	def __call__(self, environ, start_response):
		path = environ['PATH_INFO'].split('/')
		
		if len(path) != 3:
			start_response('404 Not Found', ())
			return "Not Found"
			
		eventlet.spawn(self.event, path[1], path[2])
		
		start_response('200 Ok', [])
		return json.dumps([True, {}])