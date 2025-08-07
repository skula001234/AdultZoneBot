from flask import Flask, Response
import requests
app = Flask(__name__)

@app.route('/')
def show_github_html():
    response = requests.get('https://raw.githubusercontent.com/Dypixx/live/main/index.html')
    return Response(response.text, mimetype='text/html') if response.status_code == 200 else ("Bot is LIVE", 500)

if __name__ == "__main__":
    app.run()

'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''
