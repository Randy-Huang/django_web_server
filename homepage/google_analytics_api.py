from homepage.connect_google_service import connect_google_service 

class google_analytics_api.py:
    VIEW_ID = 'ga:170802827'

    def __init__(self):
        self.service = None
        self.view_id = 'ga:170802827'
        self.startDays = 1
        self.enddays = 1

    def connect_service(self):
        if self.service is None:
            try:
               self.service = connect_google_service.get_google_service()
            except Exception, e:
               self.service = connect_google_service.get_google_service()

    def get_ga_data(self, ids=VIEW_ID, ):
        self.connect_service()
        data = self.service.data().ga().get(ids, )
