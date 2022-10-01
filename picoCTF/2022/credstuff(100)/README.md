# Credstuff


We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
Download the leak [here](./leak.tar).

The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

# solution

Wrote a quick python script to extract the flag from the files. We know the line number of the username and password are the same, so we extract the password. After a quick glance, we recognize rot13 encoding. We decode the password and capture the flag.