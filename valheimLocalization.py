from dotenv import load_dotenv
from functions import create_localization_folder

load_dotenv()

## Taken from Jotunn documentation here: https://valheim-modding.github.io/Jotunn/data/localization/language-list.html
valheim_languages = [
    "English", "Swedish", "French", "Italian", "German", "Spanish", 
    "Russian", "Romanian", "Bulgarian", "Macedonian", "Finnish", 
    "Danish", "Norwegian", "Icelandic", "Turkish", "Lithuanian", 
    "Czech", "Hungarian", "Slovak", "Polish", "Dutch", 
    "Portuguese_European", "Portuguese_Brazilian", "Chinese", 
    "Chinese_Trad", "Japanese", "Korean", "Hindi", "Thai", 
    "Abenaki", "Croatian", "Georgian", "Greek", "Serbian", 
    "Ukrainian", "Latvian"
]

## This function will generate the translation files.
create_localization_folder(valheim_languages, 'English_yourModNameHere.json', 'ExampleMod')