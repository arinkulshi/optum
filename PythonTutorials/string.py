message = "hello world"
#Count the value
count  = message.count("hello")

print(count)
#[0:5] including 0 but not including 



#Find the value
print(f'This is the value, {message.find("world")}')

#Replace this is not in place
new_message = message.replace('world','Universe')

print(new_message)


#Formatting
message = f'{message.upper()} , '

