import  os
import sys

path ='/home/venkatpodili/myresume'
if path not in sys.path:
    sys.path.append(path)

os.environ['Django_SETTINGS_MODULE'] = 'myresume.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
