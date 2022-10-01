# Buffer Overflow 0

## Description

Smash the stack

Let's start off simple, can you overflow the correct buffer? The program is available [here](./vuln). You can view source [here](./vuln.c). And connect with it using:
```sh
nc saturn.picoctf.net 53935
```

## Solution

We can overflow the buffer by putting in a string of more than 100 characters. This results in the flag being printed, due to the seg;entation fault handler printing the flag. The flag returned from the server seems to be incorrect, maybe they updated the server without updating the question.
 `man gets` shows us: 
`Never use gets(). Because it is impossible to tell without knowing the data in advance how many characters gets() will read, and because gets() will continue to store characters past the end of the buffer, it is extremely dangerous to use. It has been used to break computer security. Use fgets() instead.`