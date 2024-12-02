# Import necessary libraries
from pdf2image import convert_from_path
import pytesseract

# Section: Define Variables for File Path and Output
# Path to the PDF file
pdf_path = "C:/Users/bciez/Documents/Basilio/UCSF/WGS_Project/sum_stat/single_marker/inputs/jung_2021_sup.pdf"  # Change this to your PDF file location

# Output file path for the combined filtered text
output_text_path = "C:/Users/bciez/Documents/Basilio/UCSF/WGS_Project/sum_stat/single_marker/output/pages_34_to_39_filtered_table.txt"  # Change this to desired output path

# Section: Function to Filter Words Before the First Number in a Row
def filter_words_before_number(row):
    """
    Filters and returns words in a row before the first occurrence of a number.
    """
    filtered_row = []
    for word in row:
        if word.isdigit() or any(char.isdigit() for char in word):  # Check if the word contains a number
            break
        filtered_row.append(word)
    return filtered_row

# Section: Process PDF Pages and Extract Filtered Text
# Initialize a list to store the filtered text for all pages
filtered_texts = []

# Loop through the specified page range (pages 34 to 39, indices 33 to 38)
for page_num in range(33, 39):
    # Convert the current page to an image
    page_image = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)[0]
    
    # Perform OCR on the page image to extract text
    ocr_text = pytesseract.image_to_string(page_image)
    
    # Split the OCR text into lines
    ocr_lines = ocr_text.split("\n")
    
    # Extract and filter words before the first number for each row in the current page
    for line in ocr_lines:
        row = line.split()
        if row:  # Skip empty lines
            filtered_row = filter_words_before_number(row)
            filtered_texts.append(" ".join(filtered_row))

# Section: Save the Filtered Text to a File
# Save the combined filtered text to the output file
with open(output_text_path, "w") as file:
    file.write("\n".join(filtered_texts))

# Print the output file path for reference
print(f"Filtered text saved to: {output_text_path}")

