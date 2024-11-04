import os
import json
import csv
from androguard.misc import AnalyzeAPK

def analyze_apk(apk_path):
    apk_info, dex_code, analysis = AnalyzeAPK(apk_path)

    permissions = apk_info.get_permissions() or []
    intents = {}

    for activity in apk_info.get_activities():
        intent_filters = {
            "actions": apk_info.get_intent_filters(activity, 'action') or [],
            "categories": apk_info.get_intent_filters(activity, 'category') or [],
            "data": apk_info.get_intent_filters(activity, 'data') or [],
        }
        intents[activity] = intent_filters

    return permissions, intents

def process_apk(apk_path):
    analyzed_data = []

    permissions, intents = analyze_apk(apk_path)
    if permissions is not None and intents is not None:
        analyzed_data.append({
            'APK': os.path.basename(apk_path),
            'Permissions': permissions,
            'Intents': intents
        })

    return analyzed_data

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['APK', 'Permissions', 'Intents']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in data:
            intents_str = '; '.join([
                f"{component}: Actions: {', '.join(intent['actions']) if intent['actions'] else 'None'}, "
                f"Categories: {', '.join(intent['categories']) if intent['categories'] else 'None'}, "
                f"Data: {', '.join(intent['data']) if intent['data'] else 'None'}"
                for component, intent in entry['Intents'].items()
            ])
            writer.writerow({
                'APK': entry['APK'],
                'Permissions': ', '.join(entry['Permissions']) if entry['Permissions'] else 'None',
                'Intents': intents_str
            })

def save_to_json(data, output_file):
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    app_name = "WhatsApp"
    apk_path = f"{app_name}.apk"
    csv_path = f"{app_name}.csv"
    json_path = f"{app_name}.json"

    if os.path.exists(apk_path):
        analyzed_data = process_apk(apk_path)

        save_to_csv(analyzed_data, csv_path)
        save_to_json(analyzed_data, json_path)

        print("Data saved successfully!")
    else:
        print(f"Error: APK file '{apk_path}' not found.")
