# Vimeo
## Home Assignment

### Get started
First step, we need to log in to Vimeo to create an account.
after that, we need to register our app so we can make API calls.

### Generate an access token
Next, we generate an access token. An access token enables your app to make API requests.
In our app, on the information page, we chose Authenticated because this generates the scopes section, which offers various capabilities. check the 'private' capability to proceed and choose 'interact' so we can post and get data using API, and now click 'generate', it will give us personal access token.

### Set up a Vimeo SDK
we are setting up our development environment so we could connect and interact with the Vimeo API.
we install the package PyVimeo. Install using:
```terminal
pip install PyVimeo
```

### Usage
Now we go to write the script.
First, we need to take from the information page in our app the client identifier, client secret, and the access token that we just generated.
Next, we import the package we installed and use SDK that vimeo gave us, and put in the labels the client identifier, client secret, and the access token. 
```python
import vimeo

# setting up our client using the SDK that Vimeo gave us
client = vimeo.VimeoClient(
    token='a95fa1a2701765c16cfd4948cb69f939',
    key='6e88ecab83a228d7e99e47edf11be72fffd76478',
    secret='h2kZhYNclYU+Z4kWFuFxH0aSTzEc0/Qvz2ujBFh2203Mo78yvl8JqetP7OGg+5Zi2LFQDoBlWiSj7ezVg9h+hekbf5ZoXKdgj0feIYj8Pb7CZI6YhFCL984NRlhM3OSC'
)
```

### Make a POST request
To make comment on a video, we need to make a post request.
We take the URL from the developer tools page on the Vimeo website, put the video id, and after that comments and add the comment using dictionary.

```python
# comment on a video
comment = client.post('https://api.vimeo.com/videos/277905407/comments',
                      data={"text": "Beautiful!"})
```
### Printing the number of likes and views
To get the data that we want, we use the get method, storing the video data in a variable in a JSON format, and then we use JSONPath to filter the JSON data and find the paths of likes and views.

```
# get the data in a json format
data = client.get('https://api.vimeo.com/videos/277905407').json()
```
```
"stats": {
    "plays": 213496
  },
  ...
"metadata": {
    "connections": {
      ...
      "likes": {
        "uri": "/videos/277905407/likes",
        "options": [
          "GET"
        ],
        "total": 2651
      },
```

Lastly, we print out the number of likes and views.

```
# After filtering, getting the paths of the likes and views
likes = data['metadata']['connections']['likes']['total']
plays = data['stats']['plays']

# printing the number of likes and views
print(f'Number of likes: {likes}\n'
      f'Number of plays: {plays}')
```
