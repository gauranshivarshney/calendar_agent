from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import json
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_INFO = json.loads(os.getenv("GOOGLE_CREDENTIALS_JSON"))

credentials = service_account.Credentials.from_service_account_info(
    SERVICE_ACCOUNT_INFO, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=credentials)
calendar_id = 'primary'

def extract_time_range(text):
    # Simplified demo: customize with better NLP
    now = datetime.utcnow()
    return (now + timedelta(hours=2), now + timedelta(hours=3))

def check_availability(time_range):
    body = {
        "timeMin": time_range[0].isoformat() + "Z",
        "timeMax": time_range[1].isoformat() + "Z",
        "items": [{"id": calendar_id}]
    }
    eventsResult = service.freebusy().query(body=body).execute()
    return not eventsResult['calendars'][calendar_id]['busy']

def book_slot(time_range):
    event = {
        'summary': 'Scheduled Meeting',
        'start': {'dateTime': time_range[0].isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': time_range[1].isoformat(), 'timeZone': 'UTC'},
    }
    service.events().insert(calendarId=calendar_id, body=event).execute()