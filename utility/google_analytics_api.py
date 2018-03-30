from pandas import DataFrame
from utility.connect_google_service import SCOPE_ANALYTICS, API_ANALYTICS
from utility.connect_google_service import ConnectGoogleService

VIEW_ID = 'ga:170802827'

# https://developers.google.com/analytics/devguides/reporting/core/dimsmets
# MMetrics 
METRICS_VISITOR_COUNT = 'ga:entrances,ga:pageviews,ga:uniquePageviews'

# Dimensions 
DIMENSIONS_VISITOR_COUNT = 'ga:PagePath'

class GoogleAanalyticsService:
    def __init__(self):
        self.service = None
        self.startDays = '2018-03-08' # YYYY-MM-DD
        self.endDays = 'today'

    def connect_service(self):
        if self.service is None:            
            self.service = ConnectGoogleService(API_ANALYTICS, SCOPE_ANALYTICS, 'v3').get_google_service()

    def set_days(self, start=1, end=1):
        # start and end can specify a start date formatted as YYYY-MM-DD, or as a relative date 
        # (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.
        self.startDays = start
        self.endDays = end 

    def get_ga_data(self, ids=VIEW_ID, 
            start=None,
            end=None, 
            metrics=METRICS_VISITOR_COUNT, 
            dimensions=DIMENSIONS_VISITOR_COUNT,
            filters=None,
            max_results=None,
            **kwargs):
        self.connect_service()
        if start is None or end is None:
            start_date = self.startDays 
            end_date = self.endDays 

        if filters is not None:
            filters = 'ga:PagePath=@' + filters 

        #data = self.service.data().ga().get(ids, start_date, end_date, metrics, dimensions).execute()
        data = self.service.data().ga().get(ids=ids, start_date=start_date, end_date=end_date, metrics=metrics, dimensions=dimensions, filters=filters, max_results=max_results).execute()
        return data 

    def get_account(self):
        self.connect_service()
        data = self.service.management().accounts().list().execute()
        return data

