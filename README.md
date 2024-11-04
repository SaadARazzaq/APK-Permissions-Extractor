# APK Analysis Tool

This Python script analyzes Android APK files to extract permissions and intent filters, providing insights into the access and interactions of an app. The tool outputs the analyzed data in both CSV and JSON formats, making it easy to review permissions and intent filters for any APK file.

[![EXTRACT (1)](https://github.com/user-attachments/assets/cf00f35f-6f63-4b1c-98f6-436253ec9394)](https://www.youtube.com/watch?v=OiSrD0MxOZw)

## Features
- Extracts permissions from APK files, showing what access the app requests (e.g., location, contacts).
- Retrieves intent filters for each activity, detailing how the app interacts with other components or system actions.
- Exports results to CSV and JSON formats for easy data handling and analysis.

## Requirements
- Python 3.12 (or compatible version)
- Androguard library (for APK analysis)
- JSON and CSV libraries (built-in)

## Usage
Place the APK file in the same directory as the script and name it accordingly (e.g., `WhatsApp.apk`) and run the script.

## Example
For an APK named `WhatsApp.apk`, the script will output:
- `WhatsApp.csv` (CSV format with permissions and intents)
- `WhatsApp.json` (JSON format with permissions and intents)

## Output Format
- **CSV File**: Lists the APK name, permissions, and intents. Each intent includes actions, categories, and data elements associated with the app's activities.
- **JSON File**: Contains the same information as the CSV, formatted for easy parsing and further analysis.

## Code Overview
- `analyze_apk(apk_path)`: Analyzes the APK file for permissions and intents.
- `process_apk(apk_path)`: Collects data from the APK file and formats it for saving.
- `save_to_csv(data, output_file)`: Saves the analyzed data to a CSV file.
- `save_to_json(data, output_file)`: Saves the analyzed data to a JSON file.

## Example Output (CSV)
APK,Permissions,Intents  
WhatsApp.apk,"android.permission.CAMERA, android.permission.RECORD_AUDIO","MainActivity: Actions: android.intent.action.VIEW, Categories: android.intent.category.DEFAULT, Data: http"

## Troubleshooting
- Ensure that Androguard is installed and compatible with your Python version.
- Verify the APK file path is correct.
- If an APK file has complex security features, the analysis might be limited.

## License
This project is open-source and available for free use and modification.

```
made with 💖 by Saad Abdur Razzaq
```
