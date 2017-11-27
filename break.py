class ShortInputException(Exception):
    '''a user-defined except class'''
    def __init__(self,length,leastlen):
        Exception.__init__(self)
        self.length=length
        self.leastlen=leastlen


while True:
    try:
        s=input('enter something: ')
        if len(s)<3:
            print('length of the string=', len(s))
            raise ShortInputException(len(s),3)
        print(s)
        if s=='quit':
            break
    except EOFError:
        print("Error:end of file")
        break
    except KeyboardInterrupt:
        print("Error: operation cancelled")
        break
    except ShortInputException as ex:
        print(("ShortInputException: The input was"+
               "{0} long, expected at least {1}").format(ex.length,ex.leastlen))
    else:
        print("no exception was raised")
else:
    print('while is over')
print('done')

