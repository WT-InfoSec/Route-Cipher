# Route-Cipher
Message encryption problem from a programming assignment at Carnegie Mellon

A right-left cipher, a kind of route cipher, is a fairly simple way to encrypt a message. It takes two values, some plaintext and a number of rows, and it first constructs a grid with that number of rows and the minimum number of columns required, writing the message in successive columns. For example, if the message is WEATTACKATDAWN, with 4 rows, the grid would be: 

W T A W
E A T N

   
   
   [W T A W]
   [E A T N]
   [A C D  ]
   [T K A  ]
   (see screenshot for correct formatting)
   
We will assume the message only contains uppercase letters. We'll fill in the missing grid entries with lowercase letters starting from z and going in reverse (wrapping around if necessary), so we have:

W T A W
E A T N
A C D z
T K A y
   
Next, we encrypt the text by reading alternating rows first to the right ("WTAW"), then to the left ("NTAE"), then back to the right ("ACDz"), and back to the left ("yAKT"), until we finish all rows. We precede these values with the number of rows itself in the string. So the encrypted value for the message WEATTACKATDAWN with 4 rows is "4WTAWNTAEACDzyAKT". 

With this in mind, write the function encodeRightLeftCipher(message, rows) that takes an all-uppercase message and a positive integer number of rows, and returns the encoding as just described.

Then, write the function decodeRightLeftCipher, which takes an encoding from the previous problem and runs it in reverse, returning the plaintext that generated the encoding. For example, decodeRightLeftCipher("4WTAWNTAEACDzyAKT") returns "WEATTACKATDAWN".

------------------




