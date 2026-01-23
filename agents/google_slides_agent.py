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

    slides_service = build("slides", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    # 1️⃣ Create presentation
    presentation = slides_service.presentations().create(
        body={"title": state["topic"]}
    ).execute()

    presentation_id = presentation["presentationId"]

    # 2️⃣ Move it into your shared folder
    FOLDER_ID = "1HZWU82y-D0BpDKUS9jFDYfDCp4f3Hyt4"

    drive_service.files().update(
        fileId=presentation_id,
        addParents=FOLDER_ID,
        removeParents="root",
        fields="id, parents"
    ).execute()

    state["google_slides_id"] = presentation_id
    return state
