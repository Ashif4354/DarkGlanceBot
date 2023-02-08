import requests
class A:
    def hiscor(ph):#1
        
        url = 'https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/TN/CREATEOTP-V2'
        payload = {
  'mobileNumber': '8122763755',
  'channelPartnerID': 'MSMIND',
  'country': 'IN',
  'timestamp': '2023-02-08T16:51:58.088Z',
  'otpSize': '4',
  'loginType': 'REGISTERORSIGNIN',
  'isMobileMandatory': 'true'
}
        try:
            p = requests.post(url, data = payload)
            print(p.status_code)
        except:            
            pass

            

A.hiscor('9566782699')