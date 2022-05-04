import vimeo

# setting up our client using the SDK that Vimeo gave us
client = vimeo.VimeoClient(
    token='a95fa1a2701765c16cfd4948cb69f939',
    key='6e88ecab83a228d7e99e47edf11be72fffd76478',
    secret='h2kZhYNclYU+Z4kWFuFxH0aSTzEc0/Qvz2ujBFh2203Mo78yvl8JqetP7OGg+5Zi2LFQDoBlWiSj7ezVg9h+hekbf5ZoXKdgj0feIYj8Pb7CZI6YhFCL984NRlhM3OSC'
)
# comment on a video
comment = client.post('https://api.vimeo.com/videos/277905407/comments',
                      data={"text": "Beautiful!"})

# get the data in a json format
data = client.get('https://api.vimeo.com/videos/277905407').json()

# After filtering, getting the paths of the likes and views
likes = data['metadata']['connections']['likes']['total']
plays = data['stats']['plays']

# printing the number of likes and views
print(f'Number of likes: {likes}\n'
      f'Number of plays: {plays}')
