import openpyxl
from googletrans import Translator

# Load the workbook and select the active worksheet
file_path = "C:/Users/agutierrez/Downloads/Telegram.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Initialize the translator
translator = Translator()

# Function to translate text and handle empty cells
def translate_cell(row, source_col, target_col):
    text = sheet[f"{source_col}{row}"].value
    if text:
        try:
            # Print the current row being processed
            print(f"Translating row {row}...")
            # Ensure text is handled as UTF-8
            translated_text = translator.translate(text, dest='en').text
            # Write the translated text back to the Excel sheet
            sheet[f"{target_col}{row}"].value = translated_text
        except Exception as e:
            print(f"Error translating row {row}: {e}")

# Iterate through the rows and translate non-empty cells in Column D to Column E
for row in range(2, 109001):  # Adjust the range if your dataset has a different number of rows
    translate_cell(row, 'D', 'E')

# Save the changes to a new file, ensuring UTF-8 compatibility
workbook.save('"C:/Users/agutierrez/Downloads/TranslatedTelegram.xlsx"')

print("Translation complete and saved to 'translated_excel_file_utf8.xlsx'")
