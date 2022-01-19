from itertools import combinations
from .models import Customer_Profile


class Account:
    """
    Class for generate account number for customer
    """

    def account_number():
        """Function to generate the account number"""
        account_num = None
        fixed_num = "283848"
        last_num = ""
        com = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        for ls in com:
            for i in ls:
                last_num = last_num + str(i)
            account_num = int(fixed_num + last_num)
            if not Customer_Profile.objects.filter(account_number=account_num).exists():
                break
            else:
                last_num = ""
        return account_num
