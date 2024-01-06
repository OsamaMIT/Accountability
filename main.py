import streamlit as st
import requests 

st.set_page_config(
    page_title="Friendify",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/OsamaMIT',
        'Report a bug': "https://github.com/OsamaMIT",
        'About': "# Just have fun!"
    }
)

# Globals
friends = []
github = "GitHub"
friend_github = "GitHub"

# Other functions used

# Other pages
def login():
  'Login Page'

def add():
  newFriend = st.text_input('Friend\'s Username', placeholder='ElonMusk#0000')
  friends.append(newFriend)

def settings():
  login()
  github = st.text_input('GitHub Username', placeholder='OsamaMIT')


# Displays header & introduction
st.markdown('''<h1 style='text-align: center'> 
Accountability Platform
</h1>''', unsafe_allow_html=True)

st.markdown('''<p style='text-align: center'> 
Welcome! Ever wish you had an easier way of holding your buddy accountable, 
and vice versa? Well the future is now, thanks to science!
</p>''', unsafe_allow_html=True)



# Horizontal bar -> Inputs
row = st.columns([10,10,1.74,2.5,2.5])
with row[0]: # What to track
  # Allows selection of displayed stat
  optionTrack = st.selectbox(
  'What are you tracking?',
  ('Water Intake', 'Studying', 'GitHub') )

with row[1]: # Which Friend
  options = [f"{i}" for i in friends]
  optionFriend = st.selectbox(
  'Which friend are you tracking?',options=options)

with row[2]: # Login
  ''
  ''
  if st.button('Login'):
    login()

with row[3]: # Add Friends
  ''
  ''
  if st.button('Add Friend'):
    add()

with row[4]: # Add Friends
  ''
  ''
  if st.button('Settings'):
    settings()




# Vertical columns -> Features tracker data
col = st.columns(2)

## User Column
with col[0]:
  st.markdown("<h2 style='text-align: center'> User </h2>", unsafe_allow_html=True)

  if optionTrack == 'GitHub':
    if github == 'GitHub':
      'Add your GitHub username in your settings to see personalized data!'

    github
    url = "https://api.github.com/users/" + github
    resp = requests.get(url)
    data = resp.json()
    data


## Friends Column
with col[1]:
  st.markdown("<h2 style='text-align: center'> Friend </h2>", unsafe_allow_html=True)

  if optionTrack == 'GitHub':
    if friend_github == 'GitHub':
      'Tell your friend to add their GitHub username in their settings to see\
      personalized data!'
    
    friend_github
    url_f = "https://api.github.com/users/" + github
    resp_f = requests.get(url_f)
    data_f = resp_f.json()
    data_f