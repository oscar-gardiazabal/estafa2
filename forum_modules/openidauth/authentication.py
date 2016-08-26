from consumer import OpenIdAbstractAuthConsumer
from forum.authentication.base import ConsumerTemplateContext


class YahooAuthConsumer(OpenIdAbstractAuthConsumer):
    def get_user_url(self, request):
        return 'http://me.yahoo.com/'

class YahooAuthContext(ConsumerTemplateContext):
    mode = 'BIGICON'
    type = 'DIRECT'
    weight = 300
    human_name = 'Yahoo'
    icon = '/media/images/openid/yahoo.gif'

class MyOpenIdAuthConsumer(OpenIdAbstractAuthConsumer):
    dataype2ax_schema = {
        #'username': ('http://schema.openid.net/namePerson/friendly', 'friendly'),
        'email': 'http://schema.openid.net/contact/email',
        #'web': 'http://schema.openid.net/contact/web/default',
        #'birthdate': ('http://schema.openid.net/birthDate', 'birthDate'),
    }

    def get_user_url(self, request):
        blog_name = request.POST['input_field']
        return "http://%s.myopenid.com/" % blog_name

class MyOpenIdAuthContext(ConsumerTemplateContext):
    mode = 'BIGICON'
    type = 'SIMPLE_FORM'
    simple_form_context = {
        'your_what': 'MyOpenID user name'
    }
    weight = 400
    human_name = 'MyOpenID'
    icon = '/media/images/openid/myopenid_big.png'
    
class OpenIdUrlAuthConsumer(OpenIdAbstractAuthConsumer):
    pass

class OpenIdUrlAuthContext(ConsumerTemplateContext):
    mode = 'STACK_ITEM'
    weight = 300
    human_name = 'OpenId url'
    stack_item_template = 'modules/openidauth/openidurl.html'
    icon = '/media/images/openid/openid-inputicon.gif'
