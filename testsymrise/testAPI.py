# This is how you can use your own personal access token using requests_oauthlib library to access data from the protected resource  
from requests_oauthlib import OAuth1Session
immoscout_api = OAuth1Session('testSymriseKey',
                            client_secret='bwnkaGa8cxRvAqgs',
                            resource_owner_key='aafb1fef-5a5a-461b-8006-b61d14b4864d',
                            resource_owner_secret='qSZ7nJMeDVU1HQIxXDJ5n2pmt+1idJstXIsCf7EKMMMrgnLVU6+/s2xs8zsg4dfVMw9MEfVUtqEL5HbI9oo1i+EDEznqVAay4QZvirO4770=')  
url = 'https://rest.sandbox-immobilienscout24.de/restapi/api/offer/v1.0/user/n.nehmy@laposte.net/realestate/'  
r = immoscout_api.get(url)
print(r)
