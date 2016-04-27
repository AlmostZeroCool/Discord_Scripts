import requests # Import module called requests
import time # Import module called time
# empty line for shits and giggles
email = raw_input('[Email] ') # Ask the user for their email so we can forward it to Indian scammers
password = raw_input('Password> ') # Ask the user for their password so we can hack their twitter
avatar = 'c8b136b112473ba615bc1a416f1abdd1' # Hash to botnet into the mainframe
names = [ # Start the array called names
    'this','is just','a simple', # A few of the members of the names array
    'test to see','if I can','do this' # More members of the names array
] # End the names array
headers = { "authorization": 'your_auth_session_token_here' } # Headers to use in the HTTP... request
uniform_resource_locator = 'https://discordapp.com/api/users/@me' # The uniform resource locator to send the HTTP request to
post = { # Post data constructed in a hash called post
    'avatar': avatar, # The hash to botnet into the mainframe disquised as an avatar... whatever that is
    'email': email, # Email. Indian scammers.
    'password': password, #kek resets session. will fix later idc.
    'username': names[0], # The name of the person who used you last. Fuck that person
} # End the post hash
# Empty line?
while true: # Infinite loop
    for name in names: # Iterate through each name in the names array
        post['username'] = 'wewe' # Wait why the fuck
        meme = requests.patch(url, headers=headers, data=post) # Request a meme
        print(meme.text) # Print the meme
        time.sleep(math.pi * 38.1971863421) # Take a quick nap to rejuvenate yourself
# I really think the EOF should be somewhere around here
