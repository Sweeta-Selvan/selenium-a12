# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()

## To execute the function block, we should call the function

################################################################################

# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# sample_obj = Sample()
# # Sample.login(sample_obj)
#
# sample_obj.login()
# sample_obj.logout()
#
# ## To execute the class, we should create the object and call the attributes.

################################################################################

'''
Pytest  :   Pytest is a unit testing framework.
            Testing the small portion/small unit of the entire code is called unit testing.
            To perform unit testing in selenium, we use Pytest

            To install pytest
            Go to command prompt    -->     pip install pytest

            RULES
            *   filename should always start with test_ or end with _test
                Eg  :   test_filename.py            or          filename_test.py
            *   function names should always start with test_
                Eg  :   def test_functionname():
                            pass
            *   Class names should always start with Test
                Eg  :   class TestClassName:
                            pass

            When we follow pytest rules, pytest will automatically recognize the files, functions and classes
            which are following the pytest rules.
            So without giving the function call or creating the object for the class, the functions and classes will be executed

            To execute the pytest files
            Right click anywhere on the test_file --> open in --> terminal --> pytest test_filename.py -vs
            -v  --> Verbosity.  This gives the detailed explanation of the test_scripts
            -s  --> Scripting.  This will print all the print statements



'''

def test_login():
    print("login executing")

def test_logout():
    print("logout executing")


## collected 2 items
## test_data.py::test_login    login executing         PASSED
## test_data.py::test_logout   logout executing        PASSED






























