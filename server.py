import tornado.ioloop
import tornado.web
import os
import pymongo
import MongoLib

class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(os.path.join(os.getcwd(), 'static', 'modules', 'lyket', 'lyket.html'))
		
class ExampleHandler(tornado.web.RequestHandler):
	
	def get(self, variable_name=''):
		self.write({'results': variable_name})
<<<<<<< HEAD

class ArticleHandler(tornado.web.RequestHandler):
	def get(self):
		db=MongoLib("lyket", "articles")
		#Set number for last 10 enteries, or last N articles 
		LastN=db.getLastN(10)
		dic = {}
		dic['results'] = getLastN
		self.write(dic)


		
=======
>>>>>>> master

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