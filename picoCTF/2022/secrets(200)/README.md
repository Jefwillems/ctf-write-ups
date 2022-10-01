# secrets

We have several pages hidden. Can you find the one with the flag?
The website is running [here](http://saturn.picoctf.net:61481/).

# solution

When looking at the image on the main page, we notice it is located in a folder called secret. we try and request the folder, which brings us to another hidden page. on that page, there is a stylesheet in a relative folder `hidden`. We go there, to find yet another page with a stylesheet in a folder called `superhidden`. going to that page gives us the flag.