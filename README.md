# Security Hacking Practice
 Some practice on JSON and Client Sockets in a fun Python course
 
## This project makes use of the following libraries:
* Socket
* Json
* Itertools (earlier steps, not shown in current code)

## Application Features
* Usage: python hack.py [address] [port]
* Reads file with most common usernames online into list.
* Creates a client socket and connects to server socket on address input from CLI.
* Forms, encodes and sends JSON messages through socket until it finds the correct username for exercise.
* On this final step, we found a vulnerablity: when you send a correct string of characters as the password, even if it is not yet the complete password,
the server takes more time to respond compared to if you send a completely wrong password.
* Exploiting this vulnerability, I form the password character by character to finally find my complete username-pass combination.
* This project is actually an exercise that works only in predefined conditions within the course, but it provides some insight on some potential
security vulnerabilities.
--------------------
This project is part of the <b>JetBrains Academy Python Developer Plan</b>
