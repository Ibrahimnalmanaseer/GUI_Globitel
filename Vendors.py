import json
import os
import shutil

def load_config():
    config_file_path = 'config.json'
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as file:
            config = json.load(file)
        return config
    else:
        return None

def vendors_doc_provider(app):
    devices = load_config()

    if devices is None:
        return "Error: Config file not found or empty."

    selected_device = app.device_var.get()
    message = ''

    for key, value in devices.items():
        if key == selected_device:
            message += f'''
    =========================================
    Device: {key}
    Document_Path: {value}
    =========================================
            '''
            folder_path = value
            
            doc_directory = "C:/traces"

            try:
                files = os.listdir(folder_path)
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    shutil.copy(file_path, doc_directory)
                    message += f'Copied: {file_path} to {doc_directory}\n'
            except FileNotFoundError:
                message += f'Error: Folder not found - {folder_path}\n'

    return message






    


