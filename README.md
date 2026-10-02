🌍 Language Translation Tool

A simple and user-friendly language translation web application built with Python and Streamlit as part of my CodeAlpha Artificial Intelligence Internship.

The application allows users to enter text, select a source language and a target language, and receive the translated text through a simple web interface.

✨ Features

- 🌐 Translate text between different languages
- 🔤 Select the source and target languages
- 🖥️ Simple and interactive Streamlit interface
- ⚡️ Fast and easy-to-use translation workflow
- 📋 Displays the translated result directly in the application
- 🌍 Uses the MyMemory translation service through the "deep-translator" library

🛠️ Technologies Used

- Python — Programming language
- Streamlit — Web application framework
- deep-translator — Translation library using the MyMemory translation service

📁 Project Structure

language-translation-tool/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

🚀 Running the Application Locally

Follow these steps to run the application on your own computer.

1. Clone the repository

Open your terminal or command prompt and run:

git clone YOUR_GITHUB_REPOSITORY_URL

Then enter the project directory:

cd language-translation-tool

Replace "YOUR_GITHUB_REPOSITORY_URL" with the URL of this GitHub repository.

2. Create a virtual environment

Creating a virtual environment keeps the project's dependencies separate from other Python projects.

On Windows:

python -m venv venv

Activate it:

venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv

Activate it:

source venv/bin/activate

3. Install the required dependencies

The required Python packages are listed in "requirements.txt".

Run:

pip install -r requirements.txt

4. Run the Streamlit application

Start the application with:

streamlit run app.py

Streamlit will provide a local URL, usually similar to:

http://localhost:8501

Open that address in your web browser to use the application.

🌐 Live Demo

The application is also deployed using Streamlit Community Cloud.

👉 Live Application: [Add your Streamlit URL here]

📌 How It Works

1. The user enters the text they want to translate.
2. The user selects the source language.
3. The user selects the target language.
4. The application sends the translation request through "deep-translator".
5. The translated text is returned and displayed in the Streamlit interface.

🎯 Purpose of the Project

This project was developed as part of my CodeAlpha Artificial Intelligence Internship to gain practical experience in:

- Python application development
- Working with external libraries and APIs/services
- Building interactive web applications
- Deploying Python applications
- Using GitHub for project management and version control

🔮 Possible Future Improvements

Some features that could be added in future versions include:

- 🔊 Text-to-speech functionality
- 📋 One-click copy of translated text
- 📜 Translation history
- 🎨 Improved user interface
- 🔄 Automatic source-language detection
- 📱 Improved mobile responsiveness

👨‍💻 Author

Yosef Alene

Built as part of the CodeAlpha AI Internship — October 2026.