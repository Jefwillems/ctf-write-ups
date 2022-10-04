# SQLiLite

Can you login to this website?
Enable the question by launching an instance on the picoCTF website

# solution

upon opening the page, we try logging in with `admin` `admin`. This shows us an error page stating we weren't logged in. The page also shows us the query used to get to that result. With a simple SQL injection, we manage to log in and grab the flag.

The password used was `' OR 1 = 1;`