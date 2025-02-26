import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Ask user to select a PDF file
book = askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

if not book:  # If no file is selected, exit
    print("No file selected.")
    exit()

# Open the PDF file
pdfreader = PyPDF2.PdfReader(book)

# Get the total number of pages
numpages = len(pdfreader.pages)

# Initialize the text-to-speech engine
agent = pyttsx3.init()

# Loop through each page and read the text
for i in range(numpages):
    page = pdfreader.pages[i]
    text = page.extract_text()
    
    if text.strip():  # Only read non-empty text
        print(f"Reading page {i+1}...")
        agent.say(text)
        agent.runAndWait()  # Speak the text before moving to the next page

print("Reading complete.")