import tornado.ioloop
import tornado.web
import os

class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(os.path.join(os.getcwd(), 'static', 'modules', 'lyket', 'lyket.html'))
		
class ExampleHandler(tornado.web.RequestHandler):
	
	def get(self, variable_name=''):
		self.write({'results': variable_name})

def main():
	app = tornado.web.Application([
		tornado.web.url(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), 'static')}),
		tornado.web.url(r'/example/?(?P<variable_name>.+)?', ExampleHandler),
		tornado.web.url(r'/', HomeHandler)
	], debug=True)
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	
if __name__ == '__main__':
	main()