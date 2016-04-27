import requests # Import the module called requests
import time # Import the module called time
# Empty line to show the difference between each block of code
auth_token = raw_input('─Authorization╼') # Read the authorization token from the user
headers = { 'authorization': auth_token } # Construct the headers for the HTTP Post request into a hash
servers = [ # Begin the servers array, which stores the ids of each of the servers to send HTTP Post requests to
    '149698866541887488','106995902362689536','164183604128120832' # Each of the servers in the body of the servers array as a string
] # End the servers array
# Empty line for cleanliness 
def golang(): # Function called golang
    while true: # An infinite loop
        for server in servers: # Iterate through each server
            uniform_resource_locator = 'https://discordapp.com/api/channels/' + server + '/typing' # Construct the uniform resource locator into a string
            ruhquets = requests.post(url, headers=headers) # Perform the post ruhquets
    time.sleep(math.pi - 1) # DON'T GO BELOW 2 OR ELSE DISCORD WILL THINK YOU'RE A BUTTNET KING
# Empty line. Just like my life
golang() # Perform the function of this script
# End of file should be somewhere around here
