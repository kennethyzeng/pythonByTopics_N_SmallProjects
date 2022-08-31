###pip3 install pexpect
###Using run() method to execute a command and return its output. 
import pexpect
 
print(pexpect.run('echo hello'))



######################1 exampl#######
'''
Using spawn class
Syntax: pexpect.spawn(“rm ./dev”)
Syntax: expect(pattern, timeout=-1, searchwindowsize=-1, async_= False)
This method waits for the child process to return a given string. 
'''
import pexpect
 
# start a child  process with spawn
# It just echos  geeksforgeeks
child = pexpect.spawn("echo geeksforgeeks")
 
# prints he matched index of string.
print(child.expect(["hai", "welcome", "geeksforgeeks"]))


#################2 exampl###################
'''
Using sendline() method
Using sendline(s = ” “)
This method writes the string to the child process and also returns the number of bytes written.
'''
import pexpect
 
# Start a child process with spawn
# This process  waits for the input
# form user
child = pexpect.spawn("cat")
 
# The input to the cat process is sent
# by the sendline()
child.sendline("hai geek")
 
# prints the index of matched string
# expressing with child process
print(child.expect(["hello", "hai geek"]))