#create a calculator 
from colorama import Fore 
import time 
import sys 
import random

run_condition='True'
class Math_functions:
    def __init__(self,flnumerical,flinteger):
        self.flnumerical=flnumerical 
        self.flinteger=flinteger 
        
    def addition(self):
        ans= lambda argv:argv + self.flnumerical
        print(ans(self.flinteger))
        
    def subtraction(self):
        ans= lambda argv:argv - self.flinteger 
        print(ans(self.flnumerical))
        
    def multiplication(self):
        ans= lambda argv:argv * self.flnumerical 
        print(ans(self.flinteger))
        
    def division(self):
        ans= lambda argv:argv / self.flinteger 
        print(ans(self.flnumerical))
        
    def remainder(self):
        ans= lambda argv:argv % self.flinteger
        print(ans(self.flnumerical))
        
title='calculator\n'
txt_color=Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW
def flnumerical_input():
        global flnumerical 
        flnumerical=float(input('Decimal or whole number:'))
def flinteger_input():
        global flinteger 
        flinteger=float(input('Decimal or whole number:'))
        
        
def error_msg(txt):
    for x in txt:
     time.sleep(0.2)
     print(Fore.RED+x,flush=False)
    else:
      global reset_to_default_color 
      reset_to_default_color=Fore.RESET 
      print(f'{reset_to_default_color}')
    if txt=='':
      pass  

error_msg(txt='')
    
for txt in title:
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\t {random.choice(txt_color)}{txt.upper()}')
else:
    print(f'{reset_to_default_color}')
    while bool(run_condition):
        try:
            flnumerical_input()
            time.sleep(0.2)
            print(flnumerical)
            time.sleep(0.2)
            arithmetic_operator=str(input('arithmetic_operator:'))
            #operators:
            operator_1='+'
            operator_2='-'
            operator_3='*'
            operator_4='/'
            operator_5='%'
            equal_sign='='
            if arithmetic_operator==operator_1:
                print(f'{flnumerical} {operator_1}')
                time.sleep(0.2)
                flinteger_input()
                time.sleep(0.2)
                print(f'{flnumerical} {operator_1} {flinteger} {equal_sign}')
                math_obj=Math_functions(flnumerical=flnumerical,flinteger=flinteger)
                math_obj.addition()
            elif arithmetic_operator==operator_2:
                print(f'{flnumerical} {operator_2}')
                time.sleep(0.2)
                flinteger_input()
                time.sleep(0.2)
                print(f'{flnumerical} {operator_2} {flinteger} {equal_sign}')
                math_obj=Math_functions(flnumerical=flnumerical,flinteger=flinteger)
                math_obj.subtraction()
            elif arithmetic_operator==operator_3:
                print(f'{flnumerical} {operator_3}')
                time.sleep(0.2)
                flinteger_input()
                time.sleep(0.2)
                print(f'{flnumerical} {operator_3} {flinteger} {equal_sign}')
                math_obj=Math_functions(flnumerical=flnumerical,flinteger=flinteger)
                math_obj.multiplication()
            elif arithmetic_operator==operator_4:
                print(f'{flnumerical} {operator_4}')
                time.sleep(0.2)
                flinteger_input()
                time.sleep(0.2)
                print(f'{flnumerical} {operator_4} {flinteger} {equal_sign}')
                math_obj=Math_functions(flnumerical=flnumerical,flinteger=flinteger)
                math_obj.division()
            elif arithmetic_operator==operator_5:
                print(f'{flnumerical} {operator_5}')
                time.sleep(0.2)
                flinteger_input()
                time.sleep(0.2)
                print(f'{flnumerical} {operator_5} {flinteger} {equal_sign}')
                math_obj=Math_functions(flnumerical=flnumerical,flinteger=flinteger)
                math_obj.remainder()
            elif arithmetic_operator!=(operator_1 or operator_2 or operator_3 or operator_4 or operator_5 ):
                error_msg(txt='Invalid operator')
        except ValueError:
            error_msg(txt='Invalid value')
