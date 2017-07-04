from db_api import test


ROUTES = [
    (r"/", test.MainHandler),
    (r"/ap/", test.APInfoPersistenceHandler)
]