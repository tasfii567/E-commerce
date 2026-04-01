# ============================================================
# PASTE THIS INTO YOUR PYTHONANYWHERE WSGI FILE
# ============================================================
# In PythonAnywhere:
#   Web tab → click the WSGI configuration file link
#   Delete everything and paste this entire file
# ============================================================

import sys
import os

# Add your project directory to the sys.path
# IMPORTANT: Replace YOUR_USERNAME with your actual PythonAnywhere username
path = '/home/YOUR_USERNAME/Ecommerce-pythonanywhere'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
