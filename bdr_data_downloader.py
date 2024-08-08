import ee  # Earth Engine API
import time  # for adding delays
import google.auth  # for Google authentication
from google.oauth2.credentials import Credentials  # for handling OAuth creds
from googleapiclient.discovery import build  # for building Google API service
from googleapiclient.http import MediaIoBaseDownload  # for downloading files
from google.auth.transport.requests import Request  # for refreshing creds
from google_auth_oauthlib.flow import InstalledAppFlow  # for OAuth flow
import io  # for I/O ops
import os  # for file and directory ops

# attempt to get default Google Cloud creds
print("Attempting to get default credentials...")
try:
    credentials, project_id = google.auth.default()
    print(f"Default credentials obtained. Project ID: {project_id}")
except Exception as e:
    print(f"Error getting default credentials: {e}")

# initialize Earth Engine with specified project
print("Attempting to initialize Earth Engine...")
try:
    ee.Initialize(project="wabrdanalyzer")
    print("Earth Engine initialized successfully.")
except Exception as e:
    print(f"Error initializing Earth Engine: {e}")

# define sections of Washington Backcountry Discovery Route
# each section is defined by its bounding box coordinates
wabdr_sections = {
    "Oregon_Border_to_Packwood": [-122.0, 45.6, -121.5, 46.6],
    "Packwood_to_Ellensburg": [-121.7, 46.6, -120.5, 47.2],
    "Ellensburg_to_Cashmere": [-120.7, 47.0, -120.2, 47.5],
    "Cashmere_to_Chelan": [-120.5, 47.5, -120.0, 48.0],
    "Chelan_to_Conconully": [-120.2, 48.0, -119.5, 48.5],
    "Conconully_to_Canada": [-119.7, 48.5, -119.0, 49.0],
}


# function to authenticate with Google Drive
def authenticate_gdrive():
    creds = None
    # check if token file exists and load creds from it
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", ["https://www.googleapis.com/auth/drive.readonly"]
        )
    # if no valid creds available, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                ["https://www.googleapis.com/auth/drive.readonly"],
            )
            creds = flow.run_local_server(port=0)
        # save creds for next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


# function to download file from Google Drive
def download_file(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    # download file in chunks and print progress
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    fh.seek(0)
    # save downloaded file
    with open(file_name, "wb") as f:
        f.write(fh.read())
    print(f"File downloaded: {file_name}")


# main function to process each section and download elevation data
def main():
    # authenticate with Google Drive
    creds = authenticate_gdrive()
    service = build("drive", "v3", credentials=creds)

    # process each section of route
    for name, coords in wabdr_sections.items():
        print(f"Processing {name}...")
        # create a rectangular region of interest
        roi = ee.Geometry.Rectangle(coords)
        # get elevation data for region
        elevation = ee.Image("USGS/SRTMGL1_003").clip(roi)

        # start an EE task to export elevation data to Google Drive
        task = ee.batch.Export.image.toDrive(
            image=elevation,
            description=f"elevation_{name}",
            scale=30,
            region=roi,
            fileFormat="GeoTIFF",
        )
        task.start()

        # wait for task to complete
        while task.active():
            print("Waiting for task to complete...")
            time.sleep(30)

        # check if task completed successfully
        if task.status()["state"] == "COMPLETED":
            print(f"Task completed for {name}")

            # search for exported file in Google Drive
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
                # download file
                download_file(service, file_id, f"elevation_{name}.tif")
            else:
                print(f"File for {name} not found in Google Drive")
        else:
            print(f"Task failed for {name}")


# run main function if this script is executed directly
if __name__ == "__main__":
    main()
