
#%%
class Number:
    
    num = 10

    def __init__(self, num):

        self.num = num

        print(self.num, end='')

    def __del__(self):

        print(self.num+1)

n = Number(20)
#%%
class Number:
    
    num = 20

    def __init__(self, num=10):

        self.num = num

        print(num, end='\n')

    def __del__(self):

        self.num = 21

        print(self.num)

n = Number()

del n
# %%
class Number:
    
    num = 20

    def __init__(self, num):

        self.num = num

        print(self.num)

    def __init__(self):

        print(self.num)

n = Number(10)
# %%
class Number:
    
    num = 20

    def __init__(self, num=10):

        self.num = num

        print(num, end='')

    def __del__(self):

        self.num = 21

        print(self.num)

n = Number()

del n
# %%
