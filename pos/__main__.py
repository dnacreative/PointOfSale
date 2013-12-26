from __future__ import absolute_import

from pos.app import app
import pos.app_settings

# debug = True for debug mode (server reloads self on code changes)
app.debug = pos.app_settings.debug

# use app.run(host='0.0.0.0') to listen on all IPs
app.run()