import pandas as pd

# Define the lookup dictionary based on the provided data
locale_to_language = {
    "en": "english",
    "nb_NO": "norwegian",
    "da_DK": "danish",
    "de": "german",
    "en_GB": "british english",
    "es": "spanish",
    "es_ES": "spanish",
    "fr": "french",
    "it": "italian",
    "ja": "japanese",
    "ko": "korean",
    "nl_NL": "dutch",
    "pl": "polish",
    "pt_BR": "brazilian portuguese",
    "ru": "russian",
    "sv_SE": "swedish",
    "zh_CN": "simplified chinese",
    "zh_TW": "traditional chinese",
    "id": "indonesian"
}

# Load the spreadsheet (assume it's an Excel file for this example)
file_path = '/Users/rob/Downloads/Untitled Spreadsheet.xlsx'
df = pd.read_excel(file_path)

# Define a function to map locales to languages
def map_locale_to_language(locale):
    return locale_to_language.get(locale, "unknown")  # Default to "unknown" if locale is not in the dictionary

# Create the new 'Language Preference' column
df['Language Preference'] = df['USER_LOCALE'].apply(map_locale_to_language)

# Save the updated DataFrame back to a new Excel file
output_file_path = '/Users/rob/Downloads/Untitled Spreadsheet.xlsx'
df.to_excel(output_file_path, index=False)

print("Spreadsheet updated successfully!")
