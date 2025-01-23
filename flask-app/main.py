from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def courses():
    courses = get_courses()
    return render_template('courses.html', courses=courses)

@app.route('/courses')
def courses_json():
    courses = get_courses()
    return courses


def get_courses():
    url = 'https://nvyiwigoczwfthfiqojv.supabase.co/rest/v1/Courses?select=*'
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52eWl3aWdvY3p3ZnRoZmlxb2p2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzc1Njc0MzEsImV4cCI6MjA1MzE0MzQzMX0.wt0XqdPlmoB7NY0M3KxDS86ZvYWTWkjnfTlgqqfIyjs'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to retrieve courses'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)