# Google Photos Backup Script

This Python script allows you to download photos and videos from your Google Photos account and organize them by month-year in the same directory as the script.

## Prerequisites

1. **Google API Credentials:**
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the "Photos Library API" for your project.
   - Create credentials for your project and download the JSON file containing your client secret. Rename this file to `credentials.json` and place it in the same directory as the script.

2. **Install Dependencies:**
   - Make sure you have the required Python packages installed. You can install them using the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. **Google.py Module:**
   - Ensure that the `Google.py` module is present in the same directory as the script. This module is used for establishing a connection with the Google Photos API.

## How to Run the Script

1. **Execute the Script:**
   - Run the script by executing the following command in your terminal or command prompt:
     ```bash
     python google-photos-backup.py 
     ```

2. **Authenticate and Authorize:**
   - When you run the script for the first time, it will prompt you to authenticate and authorize the application. Follow the on-screen instructions to complete this process.

3. **Script Execution:**
   - The script will retrieve your Google Photos media items, download them, and organize them into month-year folders in the same directory as the script.

4. **Output Location:**
   - The downloaded media will be stored in a folder named `GooglePhotosBackup` in the same location where the script is executed.

## Notes and Tips

- The script is configured to download a maximum of 100 media items per page. You can adjust the `pageSize` parameter in the script to control the number of items per page.

- Ensure that your Google account has the necessary permissions to access the Google Photos API.

- If you encounter any issues or errors, refer to the script comments and the [Google Photos API documentation](https://developers.google.com/photos) for troubleshooting.

## Disclaimer

This script is provided as-is and without warranty. Use it responsibly and ensure compliance with Google's API usage policies.
