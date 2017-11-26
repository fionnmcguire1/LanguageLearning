i'''
Author: Fionn Mcguire
Date 26-11-2017
Description: Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
'''

class Solution(object):
    def accountsMerge(self, accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    emails = {}
    newAccounts = []
    checker = True
    for index,account in enumerate(accounts):
        Length = len(account)
        for email in xrange(1,Length):
            if account[email] not in emails:
                emails[account[email]]=len(newAccounts)
                checker = False
            else:
                indexOfAccount = emails[account[email]]
                if indexOfAccount != len(newAccounts):
                    checker = True
                    for index1 in xrange(1,Length):
                        if account[index1] not in newAccounts[indexOfAccount]:
                            emails[account[index1]] = indexOfAccount
                            newAccounts[indexOfAccount].append(account[index1])
        if checker == False:
            newAccounts.append(account)
            for index,account in enumerate(newAccounts):
                newAccounts[index] = [account[0]]+sorted(account[1:])
        return newAccounts
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
