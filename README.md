## Valheim GPT Localization Script

This repository contains a Python script and an equivalent Jupyter Notebook to generate localizations for mods using Jotunn or Blaxxun-boop's LocalizationManager. Both support the same JSON format.

## How to Install and Run

1. Clone this repository to your local device.
2. Install dependencies:
    - `pip install openAI`
    - `pip install python-dotenv`
3. Create an `.env` file in the root directory.
4. Sign up for a GPT API key [here](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBpUEIxZ1pVY29xaGxmRDFITWJ1MDJtSE1XYW9mTkl5UqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHV4QkpPTkg2aXlVSi13VjhrWmluMzdBaWhHZkh5RFJIo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q).
5. In your `.env` file, enter your API key as `OPENAI_API_KEY='your_api_key'`.
6. In the root directory, replace `English_yourModNameHere.json` with your base language JSON file.
7. In the valheimLocalization.py file, change the `'English_yourModNameHere.json'` argument to the file name of your base language JSON file.
8. In the valheimLocalization.py file, change the `'ExampleMod'` argument to your mod name.
8. Run the file `python valheimLocalization.py`
9. A new folder titled 'Translations' will be created in your projects root directory. 

You can generate localizations for many languages or just one. In `valheimLocalization.py`, the list `valheim_languages` contains all the languages supported by Valheim. Adjust this list to select which languages to generate. For a single language, modify the list to include only that language. To add more languages, append them to the list.