import requests

check_payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
    'rblOnlineAppLoginMode' : None,
    'txtuname' : None,
    'Button1' : 'Login'
    }

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'

def check_student_id(user_id):
    check_payload['txtuname'] = user_id
    
    check_payload['rblOnlineAppLoginMode'] = 0
    page = requests.post(fees_url, data = check_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    check_payload['rblOnlineAppLoginMode'] = 1
    page = requests.post(fees_url, data = check_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_student_rollno(user_id):
    check_payload['txtuname'] = user_id
    
    check_payload['rblOnlineAppLoginMode'] = 0
    page = requests.post(fees_url, data = check_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_student_registerno(user_id):
    check_payload['txtuname'] = user_id
    
    check_payload['rblOnlineAppLoginMode'] = 1
    page = requests.post(fees_url, data = check_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False
