"""

DEFAULT ARGUMENT:
~~~~~~~~~~~~~~~~~
    In this function, if the value is not provided then it automatically assumes the default value already given.
Considering the below function, where y is initialized with value. while calling if we give options like
def default_func_1(x=99, y=90):
    print(x, y)

default_func_1(20)  --> 20, 19
Value you can be overridden as well.
default_func_1(20,100)  --> 20, 100
If both the argumets are defined even then we can override at the time of calling the function
default_func_1(33,87)   --> 33, 87

Any number of parameters can have default value but once the default value is given then the parameters to its right side
must have values.

"""

'''

KEYWORD ARGUMENT: 
~~~~~~~~~~~~~~~~
    It is not necessary to call the function with parameters with order already defined.
Here if you do not give value to each parameter while calling then it will by default assumes that whatever value 
you have given in the order while calling the function, and it will assign to the parameter in the same order.
EX: 
def keyword_arg_fun_1(firstName, lastName,age):
    print(firstName,lastName,age)

keyword_arg_fun_1('Desai','Sumanth',22)  >> Output: Desai Sumanth 22

Parameter is passed in random order
keyword_arg_fun_1(lastName='Desai',firstName='Sumanth',age=33) >> Output: Sumanth Desai 33
'''

'''

VARIABLE LENGTH ARGUMENTS:
~~~~~~~~~~~~~~~~~~~~~~~~~
    This type of the functions are used when you do not know how many parameters need to be used.
    
There are 2 types
1. Variable length non keyword argument
2. Variable length keyword argument

1. Variable length non keyword argument: 
    ' *argvs ' is used to define this function. Any string can be used in the place of argvs. 
    Here only the values are passed while calling the function.
    Any number of values can be passed while calling this function. Also any data type values can be passed.
    
    def myNames(*argvs):
    for i in argvs:
        print(i)

myNames('tony','rony','seenu','rocky',99,[10,20,30])


2. Variable length keyword argument:
    ' **kargvs ' is used to define this function. Here both keyword and value is passed while calling this function.
    Here keys and values can be printed separately
    Methods in this function is more like dictionary.
    
    def companies(**kargvs):
    for i in kargvs.values():
        print(i)
    for k in kargvs.keys():
        print(k)
    for j in kargvs.items():
        print(j)


companies(cmp1='Google', cmp2='Facebook', cmp3='Amazon')
companies(count1=100, count2=50, count3=90)
'''


'''
PYTHON FUNCTION PASS BY REFERENCE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1. When we pass a variable to a function, a new reference to the object is created.
        def myList(a):
            a[0] = 'Text'

        sampleList = [2, 3, 4, 5]
        myList(sampleList)
        print(sampleList) >> Output: ['Text', 3, 4, 5]
    
    2. When we pass a reference and change the received reference to something else, 
       the connection between the passed and received parameter is broken.
        
        def newList(a):
            a = [100,200,300]

        test_list = [1,2,3,4]
        newList(test_list)
        print(test_list)  >> Output: [1, 2, 3, 4]
        
     3. Another example to demonstrate that the reference link is broken if we assign a new value   
        
        a) Without changing the value.
        -------------------------------
        def swap_example_1(x, y):
            temp = x
            x = y
            y = temp
            print("After swap")
            print("x:", x)
            print("y:", y)

        swap_example_1(2, 3) >> Output: x = 3, y = 2
        
        b) After changing the value.
        ------------------------------
        def swap_example_1(x, y):
            temp = x
            x = y
            y = temp
            print("Inside function x:",x)
            print("Inside function y: ",y)
        x = 10
        y = 20
        swap_example_1(2, 3)
        print("Outside function x:",x)
        print("Outside function y: ",y)
        x = 'Hi'
        y = 'Python'
        print("Value of x:",x)
        print("Value of y: ",y)
        
        >>>>>>>>>>>>> Output >>>>>>>>>>>>
        
            Inside function x: 3
            Inside function y:  2
            Outside function x: 10
            Outside function y:  20
            Value of x: Hi
            Value of y:  Python
        
'''




def myNames(tablename,*columns):
    for i in columns:
        print(i)
        temp = "create table " + str(tablename) + "("+str(i)+" varchar(20) not null, "+str(i)+" int not null primary key, "+str(i)+" int not null)"
    print(temp)



myNames("EmpDetails",'Emp_name','Age','salary','emp_id','Dept')
