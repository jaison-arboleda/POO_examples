from examples.example1 import presentation_experiment as e1
from examples.example2 import start_experiment as e2
from examples.example3 import start_experiment as e3
from examples.example4 import start_experiment as e4
from examples.example5 import start_experiment as e5
from examples.example6 import start_window as e6
from examples.example7 import start_experiment as e7
from examples.example8 import start_handler as e8
from examples.example9 import start_handler as e9

import os

if __name__ == '__main__':
    options = list(filter(lambda file: "example" in file, os.listdir("examples")))
    print(options)
    option = "example"
    option += "1"
    if option == "example1":
        e1()
    elif option == "example2":
        e2()
    elif option == "example3":
        e3()
    elif option == "example4":
        e4()
    elif option == "example5":
        e5()
    elif option == "example6":
        e6()
    elif option == "example7":
        e7()
    elif option == "example8":
        e8()
    elif option == "example9":
        e9()
    else:
        print("Other example")