import math 
  
key = "4312567"
  

def encryptMessage(msg): 
    cipher = "" 
  
   
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
  
   
    col = len(key) 
      
   
    row = int(math.ceil(msg_len / col)) 
  
  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
   
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
  
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 
  

def decryptMessage(cipher): 
    msg = "" 
  

    k_indx = 0
  

    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  

    col = len(key) 
      

    row = int(math.ceil(msg_len / col)) 
  

    key_lst = sorted(list(key)) 
  

    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  

    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  

    msg = ''.join(sum(dec_cipher, [])) 
    
      
  
    null_count = msg.count('_') 
  
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg 

n=1
while n!=3:
    n=int(input("Enter\n1. for Encoding\n2. for Decoding\n3. to quit\n"))
    if n==1:
        cipher=input("Enter the text: ")
        print(f"Encrypted Message: {encryptMessage(cipher)}")
    elif n==2:
        decipher=input("Enter the text: ")
        print(f"Decrypted Message: {decryptMessage(decipher)}")
	