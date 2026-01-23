from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def google_slides_agent(state):
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=[
            "https://www.googleapis.com/auth/presentations",
            "https://www.googleapis.com/auth/drive"
        ]
    )

    service = build("slides", "v1", credentials=creds)

    presentation = service.presentations().create(
        body={"title": state["topic"]}
    ).execute()

    presentation_id = presentation["presentationId"]
    state["google_slides_id"] = presentation_id
    return state
