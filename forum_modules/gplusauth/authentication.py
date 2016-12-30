
import os.path
import urllib
import string
import random
import json
from httplib2 import Http

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from django.conf import settings as django_settings
from forum.authentication.base import AuthenticationConsumer
from forum.authentication.base import ConsumerTemplateContext
from forum.authentication.base import InvalidAuthentication

from django.http import HttpResponseRedirect

CLIENT_SECRETS_PATH = os.path.join(django_settings.SITE_SRC_ROOT,'client_secrets.json')
CLIENT_SECRETS = json.loads(open(CLIENT_SECRETS_PATH, 'r').read())
CLIENT_ID = CLIENT_SECRETS['web']['client_id']
CLIENT_SECRET = CLIENT_SECRETS['web']['client_secret']

class GooglePlusAuthConsumer(AuthenticationConsumer):

    @staticmethod
    def _generate_random_state():
        """
        Generates a random string with length of 32 symbols, used by the
        Google+ API to prevent request forgery.
        """
        symbols = string.ascii_lowercase + string.digits
        state = ''.join(random.choice(symbols) for _ in range(32))
        return state

    def prepare_authentication_request(self, request, redirect_to):
        """
        Prepares the Google+ authentication URL and adds needed parameters
        to it, like scopes, the generated state, client ID, etc.
        """

        state = self._generate_random_state()
        # scopes = (
        #     "https://www.googleapis.com/auth/plus.login",
        #     "https://www.googleapis.com/auth/plus.profile.emails.read"
        # )
        request.session['gplus_state'] = state
        request_data = dict(
            redirect_uri="{0}{1}".format(django_settings.APP_URL, redirect_to),
            # scope="  ".join(scopes),
            scope="profile",
            state=state,
            response_type="code",
            client_id=CLIENT_ID,
            access_type="offline"
        )
        login_url = 'https://accounts.google.com/o/oauth2/auth?{0}'.format(
            urllib.urlencode(request_data)
        )
        return login_url

    def process_authentication_request(self, request):
        """
        Triggered after the Google+ authentication happened. Important
        information from it is extracted, access token and association
        keys are obtained, so that local authentication system could
        process.
        """

        parser = Http()
        login_failed_url = '/'
        if 'error' in request.GET or 'code' not in request.GET:
            raise InvalidAuthentication("No se ha podido finalizar el login")
    
        access_token_uri = 'https://accounts.google.com/o/oauth2/token'
        redirect_uri = "http://www.estafa2.com/cuenta/googleplus/hecho/"
        params = urllib.urlencode({
            'code':request.GET['code'],
            'redirect_uri':redirect_uri,
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET,
            'grant_type':'authorization_code'
        })
        headers={'content-type':'application/x-www-form-urlencoded'}
        resp, content = parser.request(access_token_uri, method = 'POST', body = params, headers = headers)

        token_data = json.loads(content)
        resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(
            accessToken=token_data['access_token']
        ))

        # raise InvalidAuthentication(content)
        google_profile = json.loads(content)

        assoc_key = google_profile['id']
        return assoc_key

    def get_user_data(self, assoc_key):
        """
        Returns user data, like username, email and real name. That data
        is forwarded to the sign-up form.
        """
        return {}


class GooglePlusAuthContext(ConsumerTemplateContext):
    mode = 'BIGICON'
    type = 'CUSTOM'
    weight = 100
    human_name = 'Google+'
    code_template = 'modules/gplusauth/button.html'
    extra_css = []

