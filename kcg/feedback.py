from requests import Session
from os import environ

feedback_url = 'http://103.249.82.135/onlinefeedback/Student_Default.aspx'   

feedback_payload = {
        'ScriptManager1': 'btngoUpdatePanel|Button1',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTc3MjI0MjAwOA9kFgICAw9kFgICAQ9kFgJmD2QWBAIDD2QWCAIVDwUyZnBzcHJlYWRzdGF0ZToxMTkwNzdhMi05ZWYzLTRkMDktYmMxYS0yYmZlNWEzM2Q1MjBkAhkPPCsAEQEMFCsAAGQCHQ8FMmZwc3ByZWFkc3RhdGU6MTIyZDNmNjctYmZhNS00NmI0LWJjMTMtNTgyNDNkYjMwM2NhZAIlD2QWBAIBDzwrABECAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudGZkDBQrAABkAgUPZBYCZg9kFgJmD2QWAgIHDxBkZBYAZAIHD2QWCgIFD2QWAgIFDwUyZnBzcHJlYWRzdGF0ZToyNDc2Mzc3ZS1jZmE0LTQzOTktYTIxYy1kY2IxYzg2Y2RmOWZkAgcPEA8WBh4NRGF0YVRleHRGaWVsZAUIY29sbG5hbWUeDkRhdGFWYWx1ZUZpZWxkBQxjb2xsZWdlX2NvZGUfAGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnZGQCCQ8PZBYCHgxhdXRvY29tcGxldGUFA29mZmQCDQ8PZBYCHwQFA29mZmQCEQ8PFgIeB1Zpc2libGVoZGQYAwUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFCUZwU3ByZWFkNAUJRnBTcHJlYWQyBQlGcFNwcmVhZDEFCFNob3dncmlkDzwrAAwBCGZkBQlncmlkdmlldzIPZ2RCKjjHz8k1YxK/EuOkdpBenWpDep/t582bogOJvUyUgQ==',
        '__VIEWSTATEGENERATOR': 'F44B6A1F,
        '__EVENTVALIDATION': '/wEdAAXReA/YN9VzYtbp5/BZbPgi/XTsdQxP2vaj7OzBgvgcw+wE2ss0gCin1hlK9g6nG/mcaVnJCN6nZnxCVQrtn+XBzfg78Z8BXhXifTCAVkevd676fBQQtBltzSPfPMgxwl6c2iZyp0rXWZri7dCdN3bp',
        'ddlClg': '13,
        'txtuname': environ['REG_NO'],
        'txtpassword': environ['DOB'],
        '__ASYNCPOST': 'true',
        'Button1': 'Login'
}

def get_payload():
    global feedback_payload

    with open('fees_login_payload.json', 'r') as f:
        fees_login_payload = json.load(f)
        #print(fees_login_payload)
    


def submit_feedback(uid, dob, stars):
        return   

        
