from django.conf import settings
from django.contrib import auth
from django.http import *
from django.contrib.auth.models import User

from datetime import datetime, timedelta

class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated():
            
            return

        try:
            if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                '''
                A timedelta object represents a duration, the difference between times.
                
                timedelta([days[, seconds[, microseconds[,
                milliseconds[, minutes[, hours[, weeks]]]]]]])
                
                All arguments are optional and default to 0.

                Only days, seconds and microseconds are stored internally.
                Arguments are converted to those units:
                
                A millisecond is converted to 1000 microseconds.
                A minute is converted to 60 seconds.
                An hour is converted to 3600 seconds.
                A week is converted to 7 days.
                '''
                auth.logout(request)
                
                #del request.session['last_touch']
                return 
        except KeyError:
            pass

        request.session['last_touch'] = datetime.now()
