# buffer overflow 1

Control the return address

## solution

I used objdump to find the address of the win function. (line 193 of [objdump.txt](./objdump.txt))

After that i wrote a python program that connects to the program with the socket library. From here on out we can input byte strings into the program, and see the address returned. The moment we inputted 48 `A`'s, we noticed the return address to be `0x41414141`, This means that we had successfully overwritten the return address. After this we replaced the last 4 bytes with the address of the win function, which gets executed because of it. The win function prints the flag.