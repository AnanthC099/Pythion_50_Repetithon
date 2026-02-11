import sys 
import traceback 

def f3(x): 
    if x < 0: 
        raise ValueError('x cannot be less than 0')
    print(x) 


def f2(y): 
    f3(y) 


def f1(z): 
    f2(z) 


def main(): 
    try: 
        f1(-100)
    except: 
        exc_name, exc_data, exc_tb = sys.exc_info() 
        print("EXCEPTION NAME:", exc_name.__name__)
        print("EXCEPTION DATA:", exc_data)
        print('-----------PRINTING TRACEBACK----------')
        traceback.print_tb(exc_tb)
        print('----------PRINTING TRACEBACK END----------')

    print('ME MELO NAHI.')


main()

