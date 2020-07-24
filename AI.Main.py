import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import configparser
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'


class Config:
    config = configparser.ConfigParser()
    config.read('settings.ini')
    # access_token = config.get('Config', 'access_token')
    # owner_id = config.get('Config', 'owner_id')
    # API_version = config.get('Config', 'API_version')
    project_id = config.get('Config', 'DIALOGFLOW_PROJECT_ID')
    lang = config.get('Config', 'DIALOGFLOW_LANGUAGE_CODE')


DIALOGFLOW_PROJECT_ID = Config.project_id
DIALOGFLOW_LANGUAGE_CODE = Config.lang
SESSION_ID = 'me'
incoming_message = ''


def dialog(incoming_message):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=incoming_message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    # print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name, "  ",
          "Detected intent confidence:", response.query_result.intent_detection_confidence)
    # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)


while incoming_message != "exit":
    incoming_message = input()
    dialog(incoming_message)
