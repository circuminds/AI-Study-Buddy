# AI Study Buddy

AI Study Buddy is a simple Streamlit app powered by OpenAI GPT-5 API that lets you:

- Ask questions on any topic  
- Generate quizzes on a topic  
- Create flashcards for study

This README guides you through setting up and running the project from scratch.

---

## Prerequisites

Before you start, make sure you have:

- Python 3.8 or higher installed  
- An OpenAI API key (sign up at [OpenAI](https://platform.openai.com/signup))  
- Git installed (optional, for cloning repo)  

---

## Step 1: Clone the Repository

If you haven’t already, clone the project repo to your local machine:

```bash
git clone https://github.com/yourusername/ai-study-buddy.git
cd ai-study-buddy
```

If starting from scratch, create a new folder and initialize a Git repo (optional):

```bash
mkdir ai-study-buddy
cd ai-study-buddy
git init
```

## Step 2: Set Up a Python Virtual Environment

```bash
Create a virtual environment for dependency isolation:
python3 -m venv venv
```

Activate the virtual environment: <br>

On Windows:
```bash
.\venv\Scripts\activate

On macOS/Linux
```bash
source venv/bin/activate
```

## Step 3: Install Required Packages
Install Streamlit and the OpenAI Python client library:

```bash
pip install streamlit openai
```

## Step 4: Configure Environment Variables for API Key
To keep your API key secure, set it as an environment variable.
1. Create a .env file with:
   
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

## Step 5: Create the Main Application File (run_app.py)
Use the 'run_app.py' script from this repository

## Step 6: Run the App Locally
Run the app using Streamlit:

```bash
streamlit run app.py

```
Open the displayed URL (usually http://localhost:8501) in your browser to use the AI Study Buddy.

## Step 7: Prepare for Deployment (not covered in this project)
1. Freeze dependencies for deployment:\
2. Deploy using Streamlit Community Cloud (free) or Heroku(paid), AWS (paid), Azure App Service(paid) etc.


For any query: <br>
contact https://circuminds.com/ 

