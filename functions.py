import json
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Function to ask OpenAI to extract mod details
def create_localization_JSON(language, JSON):
    
    prompt = f"Translate the values in this {JSON} into {language}. Your response must be in the original JSON format."

    messages = [
        {"role": "system", "content": "You are an expert translator. Your response must be in a JSON format."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=messages,
        temperature=0,
        response_format={ "type": "json_object" },
        seed=1
    )
    return response.choices[0].message.content


def create_localization_folder(language_list, json_file_path, mod_name):
    # Base directory for translations
    base_dir = os.path.join(os.getcwd(), "Translations")

    # Create the Translations directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Read JSON data from the file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        JSON_data = json.load(file)

    for language in language_list:
        # Assume create_localization_JSON returns a JSON string
        localized_json = create_localization_JSON(language, JSON_data)

        # Language specific folder
        lang_folder = os.path.join(base_dir, language)

        # Create the language folder if it doesn't exist
        if not os.path.exists(lang_folder):
            os.makedirs(lang_folder)

        # Construct file name and path
        file_name = f"{language}_{mod_name}.json"
        file_path = os.path.join(lang_folder, file_name)

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(localized_json)
            print(f"File created: {file_path}")