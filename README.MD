# bamlib
A python library that makes it easy to utilize the bank-account-microservice microservice.

bank-account-microservice on:  
[heroku](https://bank-account-microservice.herokuapp.com/api/)  
[github](https://github.com/blarmon/bank-account-microservice)

## Important note: The free heroku service I'm using shuts the server down after 30 minutes of no use.  Your first call to the server will likely be slow due to this.  If you click the heroku link above you can start the server up before you utilize the library

### Install the library from pip as below:

`pip install thebamlib`

### In your .py file import the code as below:

```
from bamlib import bamfuncs
```

## Using this library:

### Available functions

* bamfuncs.get_account()
  * Called with no parameters this function will return all accounts.  Given an account id it will return only that account.
  
  CALL:
  `print(bamfuncs.get_account())`  
  OUTPUT:
```
 [{'id': 5, 'customer': 1, 'account_type': 'savings', 'balance': '1234.56', 'interest_rate': '2.76', 'account_opened': '2018-12-  29T17:50:20.862829Z'}, {'id': 6, 'customer': 1, 'account_type': 'savings', 'balance': '1234.56', 'interest_rate': '2.76', 'account_opened': '2018-12-29T17:57:35.778662Z'}, {'id': 7, 'customer': 1, 'account_type': 'savings', 'balance': '876543.21', 'interest_rate': '2.76', 'account_opened': '2018-12-29T17:58:06.781378Z'}, {'id': 8, 'customer': 1, 'account_type': 'savings', 'balance': '1234.56', 'interest_rate': '2.76', 'account_opened': '2018-12-29T17:50:20.862829Z'}, {'id': 4, 'customer': 1, 'account_type': 'money market', 'balance': '956.00', 'interest_rate': '5.00', 'account_opened': '2018-12-28T20:35:54.186979Z'}]  
```

  
* bamfuncs.get_user()
  * Called with no parameters this function will return all accounts.  Given an account id it will return only that account.
 
  CALL:
  `print(bamfuncs.get_user())`  
  OUTPUT:
```
 [{'url': 'https://bank-account-microservice.herokuapp.com/api/users/4/', 'username': 'csiegel42', 'email': 'chris@chris.chris', 'accounts': []}, {'url': 'https://bank-account-microservice.herokuapp.com/api/users/3/', 'username': 'different_name', 'email': 'chris@chris.chris', 'accounts': []}, {'url': 'https://bank-account-microservice.herokuapp.com/api/users/1/', 'username': 'csiegel', 'email': 'christopher.siegel@dmu.edu', 'accounts': ['https://bank-account-microservice.herokuapp.com/api/accounts/4/', 'https://bank-account-microservice.herokuapp.com/api/accounts/5/', 'https://bank-account-microservice.herokuapp.com/api/accounts/6/', 'https://bank-account-microservice.herokuapp.com/api/accounts/7/', 'https://bank-account-microservice.herokuapp.com/api/accounts/8/']}]
```

* bamfuncs.delete_account()
  * Accepts an account id as a parameter and deletes that account.
 
  CALL:
  `print(bamfuncs.delete_account(5))`  
  OUTPUT:
```
 <Response [204]>
```
  
* bamfuncs.delete_user()
  * Accepts a user id as a parameter and deletes that user.
 
  CALL:
  `print(bamfuncs.delete_user(4))`  
  OUTPUT:
```
  <Response [204]>
```
  
* bamfuncs.create_account()
  * Creates a new account.  5 paramaters are accepted: customer_id (number), account_type (string), balance (number), interest_rate (number), and account_opened (datetime).  All are required, except for account_opened, which will default to datetime.now().
 
  CALL:
  `print(bamfuncs.create_account(customer_id=1,account_type='savings', balance=4500, interest_rate=2.55))`  
  OUTPUT:
```
{'id': 10, 'customer': 1, 'account_type': 'savings', 'balance': '4500.00', 'interest_rate': '2.55', 'account_opened': '2018-12-31T09:58:54.183647Z'}
```
  
* bamfuncs.create_user()
  * Creates a new user.  Parameters "username" and "email" are both strings, and are both required.  The given username and email must pass all validation requirements for usernames and emails.
 
  CALL:
  `print(bamfuncs.create_user(username='sample_user', email='sample@user.net'))`  
  OUTPUT:
```
{'url': 'https://bank-account-microservice.herokuapp.com/api/users/6/', 'username': 'sample_user', 'email': 'sample@user.net', 'accounts': []}
```

* bamfuncs.modify_account()
  * Modifies an existing account.  The first parameter given is the id of the account you wish to modify.  All of the parameters given in create_account() are modifiable.  If a new value is not specified in the parameter list then that value will not be modified.
 
  CALL:
  `print(bamfuncs.modify_account(10, account_type='checking', interest_rate=3.8))`  
  OUTPUT:
```
<Response [200]>
```
  
* bamfuncs.modify_user()
  * Modifies an existing user.  The first parameter given is the id of the user you wish to modify.  All of the parameters given in create_user() are modifiable.  If a new value is not specified in the parameter list then that value will not be modified.
 
  CALL:
  `print(bamfuncs.modify_user(6, username='sample_user_modified', email='sample@user.modified'))`  
  OUTPUT:
```
 <Response [200]>  
```
