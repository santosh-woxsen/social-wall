from flask import Flask, render_template
from src.utilities.main import CUtilities
import pandas as pd
import os

app = Flask(__name__)
obj_utils = CUtilities()

# Read the Excel file and extract tweet data
def get_tweet_data():
    # Load Excel file (ensure you have an 'excel_file.xlsx' in your project folder)
    df = pd.read_excel('excel_file.xlsx',sheet_name='dataset')
    
    # Get the first 15 rows 
    tweet_data = df[['platform','content', 'url']].head(15).to_dict(orient='records')
    return tweet_data

@app.route('/')
def index():
    tweet_data = get_tweet_data()  # Fetch the tweet data from the Excel file
    return render_template('index.html', tweet_data=tweet_data)

# def load_urls(file_path):
#     df = pd.read_excel(file_path)
#     return df.to_dict('records')

# @app.route('/')
# def index():
#     links = load_urls('Social_Media_Links.xlsx')
#     return render_template('index.html',links=links)

if __name__ == '__main__':
    app.run(debug=True)

# html_path = r'data\twitter\woxsen_20241211_1015.mhtml'
# html_path = os.path.join(os.getcwd(),'data','twitter','woxsen_20241211_1015.mhtml')
# urls = obj_utils.run_process(html_path)