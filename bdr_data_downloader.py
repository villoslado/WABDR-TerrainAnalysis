import ee
import time
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import io
import os


print("Attempting to get default credentials...")
try:
    credentials, project_id = google.auth.default()
    print(f"Default credentials obtained. Project ID: {project_id}")
except Exception as e:
    print(f"Error getting default credentials: {e}")

print("Attempting to initialize Earth Engine...")
try:
    ee.Initialize(project="wabrdanalyzer")
    print("Earth Engine initialized successfully.")
except Exception as e:
    print(f"Error initializing Earth Engine: {e}")

wabdr_sections = {
    "Oregon_Border_to_Packwood": [-122.0, 45.6, -121.5, 46.6],
    "Packwood_to_Ellensburg": [-121.7, 46.6, -120.5, 47.2],
    "Ellensburg_to_Cashmere": [-120.7, 47.0, -120.2, 47.5],
    "Cashmere_to_Chelan": [-120.5, 47.5, -120.0, 48.0],
    "Chelan_to_Conconully": [-120.2, 48.0, -119.5, 48.5],
    "Conconully_to_Canada": [-119.7, 48.5, -119.0, 49.0],
}


def authenticate_gdrive():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", ["https://www.googleapis.com/auth/drive.readonly"]
        )
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                ["https://www.googleapis.com/auth/drive.readonly"],
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    fh.seek(0)
    with open(file_name, "wb") as f:
        f.write(fh.read())
    print(f"File downloaded: {file_name}")


def main():
    creds = authenticate_gdrive()
    service = build("drive", "v3", credentials=creds)

    for name, coords in wabdr_sections.items():
        print(f"Processing {name}...")
        roi = ee.Geometry.Rectangle(coords)
        elevation = ee.Image("USGS/SRTMGL1_003").clip(roi)

        task = ee.batch.Export.image.toDrive(
            image=elevation,
            description=f"elevation_{name}",
            scale=30,
            region=roi,
            fileFormat="GeoTIFF",
        )
        task.start()

        while task.active():
            print("Waiting for task to complete...")
            time.sleep(30)

        if task.status()["state"] == "COMPLETED":
            print(f"Task completed for {name}")

            results = (
                service.files()
                .list(
                    q=f"name='elevation_{name}.tif'",
                    spaces="drive",
                    fields="files(id, name)",
                )
                .execute()
            )

            items = results.get("files", [])
            if items:
                file_id = items[0]["id"]
                download_file(service, file_id, f"elevation_{name}.tif")
            else:
                print(f"File for {name} not found in Google Drive")
        else:
            print(f"Task failed for {name}")


if __name__ == "__main__":
    main()
