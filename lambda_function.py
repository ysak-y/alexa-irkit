# coding: utf-8

import os
from ask import alexa
from constants import SWITCH_AIR_CONDITIONER_SIGNAL
from irkit.api import InternetAPI

def lambda_handler(request_obj, context=None):

    metadata = {
            }

    return alexa.route_request(request_obj, metadata)

@alexa.default_handler()
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request type """
    return alexa.create_response('Just ask')

@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    ''' Handler for LaunchRequest '''
    return alexa.create_response(message="hello")

@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!")

@alexa.intent_handler('SwitchAirConditionerIntent')
def get_recipe_intent_handler(request):
    client_key = os.environ['CLIENTKEY']
    device_id = os.environ['DEVICEID']

    print('client_key id %s device_id is %s' % [client_key, device_id])
    api = IntenetAPI()

    result = api.messages.post(SWITCH_AIR_CONDITIONER_SIGNAL, client_key, device_id)
    print("result is %s" % str(result))
    return alexa.create_response('Switch air conditioner')
