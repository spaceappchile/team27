from tastypie.api import Api

from .api import ProcessResource

api = Api(api_name='v1')

api.register(ProcessResource())

urlpatterns = api.urls
