# Mail_ChatBot
Answer back the email, according to courses in the database.

# Course Recommendation Chatbot

This project implements a course recommendation chatbot that uses OpenAI's GPT-3.5 Turbo model to provide suitable course suggestions based on user questions. The chatbot interacts with incoming emails and responds with relevant course recommendations.

## Prerequisites

- OpenAI API Key: Obtain your OpenAI API key by signing up on the OpenAI website (https://openai.com).

- Gmail API Credentials:
  - Create a new project on the Google Cloud Console (https://console.cloud.google.com).
  - Enable the Gmail API for your project.
  - Create credentials (OAuth 2.0 client ID) for a desktop application.
  - Download the credentials file and save it as `credentials.json` in the project directory.

- SQL Server Database: Set up a SQL Server database to store your course data.

## Installation

1. Clone the repository:
2. Install the required Python packages:
pip install pyodbc, requests, beautifulsoup4, google-auth google-auth-oauthlib, google-auth-httplib2, google-api-python-client, openai

3. Place the `credentials.json` file (Gmail API credentials) in the project directory.

4. Update the code with your specific configuration:
- Replace the placeholders `YOUR_OPENAI_API_KEY`, `YOUR_SERVER_NAME`, `YOUR_DATABASE_NAME`, `YOUR_USERNAME`, `YOUR_PASSWORD`, `YOUR_TABLE_NAME`, and `YOUR_SENDER_EMAIL` with your own values.

## Usage

1. Run the course data scraping script (`parse.py`) to retrieve course information from the website and store it in your SQL Server database:
2. Run the course recommendation chatbot script (`course_chatbot.py`) to start listening for incoming emails and provide course recommendations based on user questions:
3. The chatbot will automatically check for new unread emails every 10 seconds. When a new email arrives with a subject line indicating a question, the chatbot will generate a response using ChatGPT and send it back to the user.

## License



## Acknowledgments

- OpenAI for providing the GPT-3.5 Turbo model.
- Google for the Gmail API.
- The course catalog website (https://www.miuul.com) for course data.



