# agents/google_slides_agent.py
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def google_slides_agent(state):
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/presentations"]
    )

    service = build("slides", "v1", credentials=creds)

    presentation = service.presentations().create(
        body={"title": state["topic"]}
    ).execute()

    presentation_id = presentation["presentationId"]
    requests = []

    for i, slide in enumerate(state["presentation"]["slides"]):
        slide_id = f"slide_{i}"

        requests.append({
            "createSlide": {
                "objectId": slide_id,
                "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"}
            }
        })

        requests.append({
            "insertText": {
                "objectId": slide_id,
                "text": slide["title"],
                "insertionIndex": 0
            }
        })

    service.presentations().batchUpdate(
        presentationId=presentation_id,
        body={"requests": requests}
    ).execute()

    state["google_slides_id"] = presentation_id
    return state
