# --------------
##File path for the file 
file_path 
def read_file(path):
    f=open(path,'r')
    sentence=f.readline()
    f.close()
    return sentence

sample_message=read_file(file_path)


#Code starts here


# --------------
#Code starts here
file_path_1
file_path_2
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
message_1,message_2

def fuse_msg(message_a,message_b):
    ima=int(message_a)
    imb=int(message_b)
    quotient=int(imb/ima)
    return str(quotient)

#fuse_msg(message_1,message_2)
secret_msg_1=fuse_msg(message_1,message_2)



# --------------
#Code starts here
message_3=read_file(file_path_3)
message_3

def substitute_msg(message_c):
    sub="Data Scientist"
    if message_c is 'Red':sub='Army General'
    if message_c is 'Green':sub='Data Scientist'
    if message_c is 'Blue':sub='Marine Biologist'
    return sub

secret_msg_2=substitute_msg(message_3)
secret_msg_2



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
message_4,message_5

def compare_msg(message_d,message_e):
    alist=message_d.split()
    blist=message_e.split()
    c_list=(i for i in alist+blist if i not in blist)
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
secret_msg_3



# --------------
#Code starts here
message_6=read_file(file_path_6)
message_6

def extract_msg(message_f):
    a_list=message_f.split()
    even_word= lambda x:(len(x)%2==0)
    b_list=filter(even_word,a_list)
    print(b_list)
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4=extract_msg(message_6)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg=" ".join(message_parts)

final_path= user_data_dir + '/secret_message.txt'

def write_file(secret_msg,path):
    file1=open(path,'a+')
    file1.write(secret_msg)
    file1.close()

write_file(secret_msg,final_path)

secret_msg


