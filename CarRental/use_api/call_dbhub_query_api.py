# encode SQL to base64 string
import base64, requests
#from requests_oauthlib import OAuth1
sql = "select * from flights"
sql_bytes = sql.encode("ascii")
sql_base64 = base64.b64encode(sql_bytes)
sql_string_b64 = sql_base64.decode("ascii")
print(sql_string_b64)

# doc: https://api.dbhub.io/#query
url = "https://api.dbhub.io/v1/query"
key = "1wKnhdHEL9dPtfk9kwmQrCBfi6b"
dbowner = "iuncis"
dbname = "flight_pub.db"
#headers = {'Content-type':"text/plain; charset=utf-8"}    
#headers = {'Authorization': f'Bearer {key}', 'Content-type':"application/json"}    
session = requests.Session()
#session.headers.update(headers)

result = session.post(f"{url}?apikey=1wKnhdHEL9dPtfk9kwmQrCBfi6b&dbowner=iuncis&dbname=flight_pub.db&sql=c2VsZWN0ICogZnJvbSBmbGlnaHRz")

print(result.json())

"""
data = {
       'apikey': key,
       'dbowner': dbowner,
       'dbname': dbname,
       'sql': sql_string_b64
}
result = session.post(url, params=data)
"""

 
