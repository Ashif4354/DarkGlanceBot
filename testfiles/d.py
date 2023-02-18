import requests
class A:
    def hiscor(ph):#1
        
        url = 'https://api.whitehatjr.com/api/V1/otp/generate?deviceId=ab5f7c2a-de52-4a6a-aba9-0d93fe1447d4&timezone=Asia/Calcutta&trackingCode=trackingCode|AB-11169-V-B|AB-11159-V-A|AB-11140-V-A|AB-11164-V-A|AB-11194-V-B|AB-11137-V-A|AB-11186-V-A|AB-11208-V-B|AB-11167-V-A|AB-11182-V-B|AB-22-V-B|AB-11188-V-B|AB-11150-V-B|AB-29-V-B|AB-11192-V-A|AB-11142-V-A|AB-11183-V-B|AB-24-V-C|AB-11151-V-B|AB-11154-V-A|AB-11200-V-A|AB-11198-V-A|AB-26-V-B|AB-11136-V-A|AB-11152-V-B|AB-11166-V-A|AB-13-V-B|AB-11195-V-A|AB-11196-V-A|AB-18-V-A|AB-11184-V-A|AB-11206-V-B|AB-31-V-A|AB-11193-V-B|AB-11176-V-B|AB-11191-V-B|AB-11181-V-B|AB-11156-V-A|AB-11209-V-A|AB-28-V-B|AB-15-V-A|AB-34-V-A|AB-11204-V-A|AB-11163-V-A|AB-11201-V-B|AB-25-V-B|AB-11135-V-A|AB-11155-V-A|AB-11202-V-A|AB-21-V-C|AB-11161-V-A|AB-37-V-B|AB-23-V-C|AB-11153-V-B|AB-17-V-A|AB-11175-V-A|AB-11165-V-A|AB-12-V-A|AB-11160-V-B|AB-27-V-B&regionId=IN&courseType=ALL&brandId=whitehatjr&timestamp=1676716225213&_vercel_no_cache=1'
        payload = {
            "dialCode": "+91",
            "mobile": "9566782699",
            "type": "voice"
        }        
        try:
            p = requests.post(url, data = payload)
            print(p.status_code)
            print(p.text)
        except:            
            pass

            

A.hiscor('9952133321')