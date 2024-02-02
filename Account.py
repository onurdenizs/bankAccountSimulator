import datetime


"""This module contains all the necessary classes for bankAccountSimulator."""

class Account:
    """Bank account class.

    This class will simulate an account with various methods.
    """
    id = 0
    activeAccountList = list()
    closedAccountList = list()

    def __init__(self, owner, currency):
        """Creates an account and appends it to the Account Class' accountList class property.
    
    Parameters
    ----------
    owner : client
        Owner of the bank account
    currency : currency
        currency type of the account

    Returns
    -------
    
    """        
        Account.id += 1
        self.owner = owner
        self. balance = 0.0
        self.currency = currency
        self.accountNumber = Account.id
        self.balance = 0
        self.owner.activeAccountList.append(self)
        self.transactionList = list()
        Account.activeAccountList.append(self)
    
    def __str__(self):
        return f'{self.owner.name} {self.owner.surname}\'s account. Current Balance is: {str(self.balance)} {self.currency.symbol}'
    
    def __repr__(self):
        return f'Account(\'{self.owner}\', {self.currency})'

    
    def setBalance(self, newBalance):
        """ Changes accounts instance attribute 'balance' with the given value
    
        Parameters
        ----------
        newBalance : float
            New Balance Value
    
        """
        self.balance = newBalance

    def deposit(self, depositAmount):
        """Adds the given amount of money to the account's balance.
        First creates a deposit type transaction then adds this transaction to the account's transactionList.
    
        Parameters
        ----------
        depositAmount : float
            Amount of money to be added to the account balance
    
        """
        newTransaction = withdrawDepositTransaction(self, depositAmount)
        newTransaction.applyDepositWithdraw()
        
        
        
    
    def withdraw(self, withdrawAmount):
        """Deducts the given amount of money from the account's balance.
    
    Parameters
    ----------
    withdrawAmount : float
        Amount of money to be deducted from the account balance
    
    """
        newTransaction = withdrawDepositTransaction(self, (-1*withdrawAmount))
        newTransaction.applyDepositWithdraw()

class Client:
    """Client  class.

    This class will simulate an account with various methods.
    """
    id = 0
    clientList = list()

    def __init__(self, name, surname, gender, birthYear, birthMonth, birthDay, nationalId):
        """Creates a client and appends it to the Client Class' clientList class property.
    
    Parameters
    ----------
    name : str
        Client Name
    surname : str
        Client Surname
    birthYear : int
        Client birth Year (ex: 1985)
    birthMonth : int
        Client birth Month between 1-12
    birthDay : int
        Client birth Day between 1-31
    nationalId : int
        Client national ID number

    Returns
    -------
    
    """
        Client.id += 1
        self.name = name
        self.surname = surname
        self.birthDate = datetime.datetime(birthYear, birthMonth, birthDay)
        currentYear = int(datetime.datetime.today().year)
        self.age = currentYear - birthYear
        self.id = Client.id
        self.activeAccountList = list()
        self.closedAccountList = list()
        self.nationalId = nationalId
        self.gender = gender
        Client.clientList.append(self)

    def __str__(self):
        return f'Name: {self.name} {self.surname}\ Age: {self.age}. Number of Active Accounts: {str(len(self.activeAccountList))} Number of Closed Accounts: {str(len(self.closedAccountList))}'
    
    def __repr__(self):
        return f'Client(\'{self.name}\', \'{self.surname}\', {self.birthDate}, {self.age})'

class Currency:
    """Currency class.

    This class will simulate a currency with various methods.
    """
    id = 0
    currencyList = list()

    def __init__(self, title, symbol, shortForm):
        """Creates a currency and appends it to the Currency Class' currencyList class property.
    
    Parameters
    ----------
    title : str
        Title of the currency (ex: United States Dollar)
    symbol : str
        Symbol of the Currency (ex: $)
    shortForm : str
        3 Letters short form of the Currency (ex: USD)
    
    Returns
    -------
    
    """
        Currency.id +=1 
        self.title = title.upper()
        self.symbol = symbol
        self. shortForm = shortForm.upper()
        self.id = Currency.id
        Currency.currencyList.append(self)

class Transaction:
    """Transaction class.

    This class will simulate transactions with various methods.
    """
    
    def __init__(self, account):
        """Parent of transaction types
        
        Parameters
        ----------
        account = Account()
            account that will transaction is applied
        
        Returns
        -------
        
        """
        
        self.date = datetime.datetime.today()
        self.account = account
    
    def applyDepositWithdraw(self):
        """Applies given transaction to the transaction's account. 
        
        Parameters
        ----------
        
        Returns
        -------
        
        """
        newBalance = AccountArithmetics.calculateNewBalance(self.account.balance, self.amount)
        self.lastBalance = newBalance
        self.account.setBalance(newBalance)
        self.account.transactionList.append(self)
    
    def applyWithdraw(self):
        """Applies given transaction to the transaction's account. 
        
        Parameters
        ----------
        
        Returns
        -------
        
        """
        newBalance = AccountArithmetics.calculateNewBalance(self.account.balance, (-1 * self.amount))
        self.lastBalance = newBalance
        self.account.setBalance(newBalance)
        self.account.transactionList.append(self)
        

class withdrawDepositTransaction(Transaction):

    def __init__(self, account, amount):
        """Child of transaction class. Deposit or Withdrawtype of transactions. 
        
        Parameters
        ----------
        account = Account()
            account that will transaction is applied
        amount = float
            Amount of money that is added or deducted to the account's balance
        Returns
        -------
        
        """
        super().__init__( account)
        self.amount = amount
        self.previousBalance = self.account.balance
        self.lastBalance = 0
    
    def __str__(self):
        transactionType = "Transaction Type"
        if self.amount > 0:
            transactionType = "Deposit"
        else:
            transactionType = "Withdraw"
        formattedDate = self.date.strftime('%d/%m/%Y, %H:%M:%S')
        return f'Transaction Type: {transactionType} Amount: {str(self.amount)}{self.account.currency.symbol} Date: {formattedDate} Previous Balance: {str(self.previousBalance)} Updated Balance: {str(self.lastBalance)}'

class AccountArithmetics:

    def calculateNewBalance(currentBalance, amount):
        """Calculates  and returnsnew balance from currentBalance and amount values.
        
    
        Parameters
        ----------
        amount : float
            Amount of money to be added to the account balance
        Returns
        -------
        newBalance = float
            Calculated new balance
        """
        depositInCents = amount * 100
        balanceInCents = currentBalance * 100 + depositInCents
        newBalance = float("{:.2f}".format(balanceInCents/100))
        return newBalance        





