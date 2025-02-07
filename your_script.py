import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
api_key = os.getenv('API_KEY')
ticker = os.getenv('TICKER')
keyword = os.getenv('KEYWORD')
