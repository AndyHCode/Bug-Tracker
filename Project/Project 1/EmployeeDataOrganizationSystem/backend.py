# importing the pandas library
import pandas as pd, re , random

def reader():
    ''' reading the csv file '''
    df = pd.read_csv("people-100.csv")
    return df


def phone_number(number):
    ''' phone number check function '''
    if len(number) < 10 or len(number) > 10:
        return False
    else:
        for char in number:
            if char.isnumeric() == False:
                return False
        else:
            return True



def check_email(email):  
    ''' this program checks the registry to make sure the email is formated properly '''
    registry = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    
    if re.match(registry, email):
        ''' if the email is valid it returns true '''
        return True
    else:
        '''else returns false'''
        return False


def social():
    ''' social security number generator '''
    social_security_number = ''
    temp_num_str = ""
    for x in range(9):
        temp_num_str = temp_num_str + str(random.randint(0, 9))
    temp_num_str = temp_num_str[0:3] + "-" + temp_num_str[3:5] + "-" + temp_num_str[5:9]
    social_security_number = temp_num_str
    return social_security_number



def id_maker():  
    ''' username generator '''
    df = reader()
    special_str = "1234567890"
    normal_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user = ''
    temp_user = ""
    
    ''' a forloop to generate 10-15 chars username '''
    for _ in range(random.randint(10, 15)):
        '''pick if char is special or normal'''
        temp_num = random.randint(0, 2)
        if temp_num != 1:
            temp_user = temp_user + random.choice(normal_str)
            continue
        temp_user = temp_user + random.choice(special_str)
    ''' add tempPassword to password list'''
    user = temp_user
    return user



def phone_format(num):
    '''formats the phone to ###-###-####'''
    df = reader()
    hold = num
    ''' formatting the number to include the dashes'''
    phone = '{}-{}-{}'.format(hold[:3], hold[3:6], hold[6:])  
    return phone



def adder(first, last, sex, email, phone, ssn):
    '''inserting the user input into the csv file'''
    df = reader()
    '''generating our username'''
    username = id_maker() 
    '''formating the phone number'''
    phone = phone_format(phone)
    '''setting up the index'''
    ind = len(df.index) + 1
    '''storing the parameters into a dictionary''' 
    new = { 
        'Index': [ind],
        'User ID': [username],
        'First Name': [first],
        'Last Name': [last],
        'Sex': [sex],
        'Email': [email],
        'Phone': [phone],
        'ssn': [ssn],
    }
    '''creating a dataframe out of our dictionary'''
    of = pd.DataFrame(new) 
    '''writing the dataframe into a CSV file'''
    of.to_csv("people-100.csv", mode='a', index=False, header=False) 
    df = pd.read_csv("people-100.csv")
    print(df)
    return username



def search_engine(csv_column, user_input):
    '''our search function'''
    df = reader()
    of = ""
    '''checking for User Input in that column and then storing result into string'''
    of += df[df[csv_column].str.match(user_input, na=False, case=False)].to_string(index=False) 
    if(of[0:15] == "Empty DataFrame"):
        return "No matching Data"
    return of



def resetter(dx):
    '''this resetter function deletes all the rows and then restores the csv back to its original state'''
    df = reader()
    i = len(df.index)
    while i != 0:
        ''' deleting each row 1 by 1 ''' 
        df.drop(i - 1, axis=0, inplace=True)
        df = df.reset_index(drop=True)
        j = i - 1
        for j in range(len(df.index)):
            df.loc[j, 'Index'] = j + 1
        df.to_csv("people-100.csv", index=False)
        i = i - 1
    ''' restoring the original file before any edits were made'''
    dx.to_csv("people-100.csv", index=False)
    df = pd.read_csv("people-100.csv")


def delete_row(num=""):
    '''This function deletes the row'''
    df = reader()

    y = len(df.index)
    if not num.isnumeric():
        return "Error: " + num +" is not a number"
    x = int(num)
    ''' this checks to make sure the user doesn't pick a number larger than the index size'''
    if (x - 1 > y - 1 or x - 1 < 0):  
        return "Error: index at " + num + " does not exist"
    
    else:
        '''deleting the row and resetting our index'''  
        z = (df.iloc[x - 1, 0:7].to_string(header=True))
        df.drop(x - 1, axis=0, inplace=True)
        df = df.reset_index(drop=True)
        i = x - 1
        for i in range(len(df.index)):
            df.loc[i, 'Index'] = i + 1
        df.to_csv("people-100.csv", index=False)
    return z

# importing the pandas library
import pandas as pd, re , random

def reader():
    ''' reading the csv file '''
    df = pd.read_csv("people-100.csv")
    return df


def phone_number(number):
    ''' phone number check function '''
    if len(number) < 10 or len(number) > 10:
        return False
    else:
        for char in number:
            if char.isnumeric() == False:
                return False
        else:
            return True



def check_email(email):  
    ''' this program checks the registry to make sure the email is formated properly '''
    registry = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    
    if re.match(registry, email):
        ''' if the email is valid it returns true '''
        return True
    else:
        '''else returns false'''
        return False


def social():
    ''' social security number generator '''
    social_security_number = ''
    temp_num_str = ""
    for x in range(9):
        temp_num_str = temp_num_str + str(random.randint(0, 9))
    temp_num_str = temp_num_str[0:3] + "-" + temp_num_str[3:5] + "-" + temp_num_str[5:9]
    social_security_number = temp_num_str
    return social_security_number



def id_maker():  
    ''' username generator '''
    df = reader()
    special_str = "1234567890"
    normal_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user = ''
    temp_user = ""
    
    ''' a forloop to generate 10-15 chars username '''
    for _ in range(random.randint(10, 15)):
        '''pick if char is special or normal'''
        temp_num = random.randint(0, 2)
        if temp_num != 1:
            temp_user = temp_user + random.choice(normal_str)
            continue
        temp_user = temp_user + random.choice(special_str)
    ''' add tempPassword to password list'''
    user = temp_user
    return user



def phone_format(num):
    '''formats the phone to ###-###-####'''
    df = reader()
    hold = num
    ''' formatting the number to include the dashes'''
    phone = '{}-{}-{}'.format(hold[:3], hold[3:6], hold[6:])  
    return phone



def adder(first, last, sex, email, phone, ssn):
    '''inserting the user input into the csv file'''
    df = reader()
    '''generating our username'''
    username = id_maker() 
    '''formating the phone number'''
    phone = phone_format(phone)
    '''setting up the index'''
    ind = len(df.index) + 1
    '''storing the parameters into a dictionary''' 
    new = { 
        'Index': [ind],
        'User ID': [username],
        'First Name': [first],
        'Last Name': [last],
        'Sex': [sex],
        'Email': [email],
        'Phone': [phone],
        'ssn': [ssn],
    }
    '''creating a dataframe out of our dictionary'''
    of = pd.DataFrame(new) 
    '''writing the dataframe into a CSV file'''
    of.to_csv("people-100.csv", mode='a', index=False, header=False) 
    df = pd.read_csv("people-100.csv")
    print(df)
    return username



def search_engine(csv_column, user_input):
    '''our search function'''
    df = reader()
    of = ""
    '''checking for User Input in that column and then storing result into string'''
    of += df[df[csv_column].str.match(user_input, na=False, case=False)].to_string(index=False) 
    if(of[0:15] == "Empty DataFrame"):
        return "No matching Data"
    return of



def resetter(dx):
    '''this resetter function deletes all the rows and then restores the csv back to its original state'''
    df = reader()
    i = len(df.index)
    while i != 0:
        ''' deleting each row 1 by 1 ''' 
        df.drop(i - 1, axis=0, inplace=True)
        df = df.reset_index(drop=True)
        j = i - 1
        for j in range(len(df.index)):
            df.loc[j, 'Index'] = j + 1
        df.to_csv("people-100.csv", index=False)
        i = i - 1
    ''' restoring the original file before any edits were made'''
    dx.to_csv("people-100.csv", index=False)
    df = pd.read_csv("people-100.csv")


def delete_row(num=""):
    '''This function deletes the row'''
    df = reader()

    y = len(df.index)
    if not num.isnumeric():
        return "Error: " + num +" is not a number"
    x = int(num)
    ''' this checks to make sure the user doesn't pick a number larger than the index size'''
    if (x - 1 > y - 1 or x - 1 < 0):  
        return "Error: index at " + num + " does not exist"
    
    else:
        '''deleting the row and resetting our index'''  
        z = (df.iloc[x - 1, 0:7].to_string(header=True))
        df.drop(x - 1, axis=0, inplace=True)
        df = df.reset_index(drop=True)
        i = x - 1
        for i in range(len(df.index)):
            df.loc[i, 'Index'] = i + 1
        df.to_csv("people-100.csv", index=False)
    return z

