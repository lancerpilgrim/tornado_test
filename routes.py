from db_api import ap_info_persistence_handler


ROUTES = [
    (r"/", ap_info_persistence_handler.MainHandler),
    (r"/ap/", ap_info_persistence_handler.APInfoPersistenceHandler)
]