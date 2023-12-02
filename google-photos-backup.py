import os
from datetime import datetime
from Google import Create_Service
import requests

# Function to create service
def create_google_photos_service(client_secret_file, api_name, api_version, scopes):
    service = Create_Service(client_secret_file, api_name, api_version, scopes)
    return service

# Function to download file
def download_file(url, destination_folder, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        print('Downloading file {0}'.format(file_name))
        with open(os.path.join(destination_folder, file_name), 'wb') as f:
            f.write(response.content)

# Function to organize media files by month-year
def organize_media_by_month_year(media_files, destination_folder):
    for media_file in media_files:
        file_name = media_file['filename']
        date_created = media_file.get('mediaMetadata', {}).get('creationTime')

        if date_created:
            # Updated format string
            date_created = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%SZ')

            month_year_folder = os.path.join(destination_folder, date_created.strftime('%Y-%m'))
            
            if not os.path.exists(month_year_folder):
                os.makedirs(month_year_folder)

            download_url = media_file['baseUrl'] + '=d'
            download_file(download_url, month_year_folder, file_name)

def main():
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'photoslibrary'
    API_VERSION = 'v1'
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

    # Create Google Photos service
    service = create_google_photos_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Retrieve all media items
    media_files = []
    page_token = None
    while True:
        response = service.mediaItems().search(body={'pageSize': 100, 'pageToken': page_token}).execute()
        media_files.extend(response.get('mediaItems', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break

    # Destination folder for downloaded content
    destination_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'GooglePhotosBackup')

    # Organize media files by month-year
    organize_media_by_month_year(media_files, destination_folder)

if __name__ == "__main__":
    main()
