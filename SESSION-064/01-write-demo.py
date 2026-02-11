import os 

s = "Hello,World\n"
print('type(s):', type(s))

msg_byte_arr = s.encode() 
print(f'type(msg_byte_arr):{type(msg_byte_arr)}')

STD_OUTPUT_DEVICE_DESCRIPTOR = 1 
os.write(STD_OUTPUT_DEVICE_DESCRIPTOR, msg_byte_arr)

L = [10, 20, 30, 40]

str_L = str(L) + "\n" 
L_byte_arr = str_L.encode() 
os.write(STD_OUTPUT_DEVICE_DESCRIPTOR, L_byte_arr)  