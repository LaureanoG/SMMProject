from googleapiclient.discovery import build

api_key = #enter your API key here

service = build('youtube', 'v3', developerKey= api_key)

request = service.search().list(q='AmongUs', part='snippet', order='viewCount', type='video')

response = request.execute()

print(response)