# AutoE
A program that allows you to send the same email to multiple people on a time delay (100 secs) and with mail merging.

Only works if you send from a gmail account and you also need to turn your "less secure app" access on in your gmail account which you can do from your securitysettings. 

Recipients should be placed in a 2 column csv file, first column heading = "names" and the second = "emails".  Save your csv file in the same folder you save the AutoE python file.  

Before running the program, you'll need to go through the code and enter some information particular to your email campaign. UPDATE:
        *The email address you are sending from
        *The password for that email address
        *The name of the csv file with your recipients
        *The subject of the email you're sending
        *The body of the email you're sending.

Emails can be tailored to feel personal.  Use .format to add in recipients name or any other variable you include in your file.

AutoE.py is the only file you need to download.  Save on computer in same folder as recipient list. Run on terminal with python3:  python3 AutoE.py


