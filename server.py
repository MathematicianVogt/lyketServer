import tornado.ioloop
import tornado.web
import os
import pymongo

class HomeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(os.path.join(os.getcwd(), 'static', 'modules', 'lyket', 'lyket.html'))

class ArticleHandler(tornado.web.RequestHandler):
	def get(self):
		
		db = pymongo.MongoClient()
		
		self.write({'results': list(db.lyket.articles.find({}, {'_id': 0}).limit(10))})

def main():
	app = tornado.web.Application([
		tornado.web.url(r'/articles', ArticleHandler),
		tornado.web.url(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), 'static')}),
		tornado.web.url(r'/', HomeHandler)
	], debug=True)
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	
if __name__ == '__main__':
	main()