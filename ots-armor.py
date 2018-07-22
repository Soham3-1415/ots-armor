import base64
import sys
    
def binaryToAscii(input_file,output_file=''):
    file = open(input_file,'rb')
    binary = file.read()
    file.close()
    message_binary = base64.b64encode(binary)
    message = message_binary.decode('utf-8')
    n=64
    message_array = [message[i:i+n] for i in range(0, len(message), n)]
    message = ''
    for i in range(0,len(message_array)):
        message = message + message_array[i] + '\n'
    message = beginString + message + endString
    message_binary = message.encode('utf-8')
    if(output_file == ''):
        print(message)
    else:
        file = open(output_file,'a')
        file.write(message)
        file.close()
    
def asciiToBinary(input_file,output_file=''):
    file = open(input_file,'rb')
    message_binary = file.read()
    file.close()
    message = message_binary.decode('utf-8')
    startIndex = message.find(beginString)
    endIndex = message.find(endString)
    message = message[startIndex + len(beginString):endIndex-1]
    message_binary = message.encode('utf-8')
    binary = base64.b64decode(message)
    if(output_file == ''):
        print(binary)
    else:
        file = open(output_file,'xb')
        file.write(binary)
        file.close()

def start():
    input_file = sys.argv[1]
    if(len(sys.argv) >= 3):
        output_file = sys.argv[2]
    else:
        output_file = ''
    if(input_file[len(input_file)-4:] == '.ots'):
        binaryToAscii(input_file,output_file);
    else:
        if(output_file != ''):
            if(len(output_file) < 4 or output_file[len(output_file)-4:] != '.ots'):
                output_file = output_file + '.ots'
        asciiToBinary(input_file,output_file)

beginString = '-----BEGIN OPENTIMESTAMPS TIMESTAMP-----\n\n'
endString = '-----END OPENTIMESTAMPS TIMESTAMP-----\n'
start()
