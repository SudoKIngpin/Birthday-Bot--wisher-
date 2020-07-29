import smtplib         #Importing all modules 
import datetime 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''Taking out date and converting it 
into string for comparison '''
today=datetime.datetime.now().strftime('%d-%m')
Imp=[] #List for storing whose birthday date matches with current date
addr=''#Empty strings for 
name='' #holding friend email ,name,
msg='' # and message




bot_id='youremail@gmail.com' #Your Gmail id for sending birthday wishes


bot_pwd='your password'#Your password for your gmail id.

#Do remember to turn on less secure apps 
#Using link : https://myaccount.google.com/lesssecureapps



message=MIMEMultipart()
message["From"]=bot_id
message["Subject"]='Happy Birthday dear Bestie'

# print(today,type(today))

Bday={'Harsh':'30-07',
'Hardik':'1-09',   #Dictionary for holding friends name with their 
'Khush':'18-05',  # Birthday dates in string type.   
'Manish':'15-06'} #Manipulate dictionary with your Friends name and bday dates



Gmail={'Harsh':'shv@gmail.com',
'Khush':'khush@gmail.com', #Dictionary for holding friends name 
'Manish':'manish@gmail.com',#with their Gmail id in string type.
'Hardik':'Hardik@gmail.com'
}


for i in Bday:   #Iterating through all Birthday dates to check if bday is today!!
    if Bday[i]==today:
        Imp.append(i)



if len(Imp)==1: #If only 1 Birthday is today!
    for i in Imp:
        addr=Gmail[i]
        name=i
    msg=f'Many many Happy returns of the day. Happy Birthday {name}. May god bless you'
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()     #SMTP PROTOCOL #tRANSPORT seCUIRITY LAYER ENCRYPTION
    server.ehlo()      #Extended time 
    server.login(bot_id,bot_pwd)
    message["To"]=addr
    body=msg
    message.attach(MIMEText(body,'plain'))
    text=message.as_string()
    server.sendmail(bot_id,addr,text)
    server.close()
    print(f' Today is {name} birthday MAil sended successfully to {name}')
    
elif len(Imp)>1: #if more than 1 birthday is today!
    for i in Imp: #Iterating through all Bday dates.
        name=i
        addr=Gmail[i] 
        msg=f'Many many Happy returns of the day. Happy Birthday {name}. May god bless you'
        message["To"]=addr
        body=msg
        message.attach(MIMEText(body,'plain'))
        text=message.as_string()
        server=smtplib.SMTP('smtp.gmail.com',587)

        server.ehlo()           #SMTP PROTOCOL
        server.starttls()
        server.login(bot_id,bot_pwd)
        server.sendmail(bot_id,addr,text)
        server.quit()
        print(f'Today is {name} Birthday, Mail sended Successfully ')
        
#If no birthday is today
else:
    
    print('No birthdays today !')
if len(addr) and len(body) and len(msg) and len(text) and len(Imp) and len(name)>0:

        del addr
        del body
        del name 
        del Imp 
        del text
        del msg



