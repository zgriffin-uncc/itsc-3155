message = input("Enter String:")
string_output = (message[0:2]+message[4:])

if (len(message)<2):{
    print("Your string is too short!")
}
else:{
    print(string_output)
}