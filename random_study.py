#This will be a random study generator. It will generate a random topic for me to study in python.
def restart():
        import random, time
        py_study = ['If else statements', 'For in loops', 'While loops', 'String concatenation', 'Casting data types','List comprehension', 'Operators', 'Functions',]
        z = random.choice(py_study)
        y = 0
        study = input('Are you ready to study? ').lower()
        time. sleep(1)
        while y < 1:
                if study == 'yes':
                        print('Ok then study:',z)# Fixed: added ",z"  !TODO: this prints every letter on a seperate line, fix it to print all on a single line 1-2-19
                        y += 1
                else:
                        print('Good bye!')
                        break
                keep_study = input(f'Good job at studing {z}, would you like a new subject? ').lower()
                time.sleep(1)
                if keep_study == 'yes':
                        restart()
                else:
                        print('Good bye!')
restart()
        


#This is what I started with, but I defined a function (restart) to take care of the code in case I need to use it elsewhere.
# import random, time
# py_study = ['If else statements', 'For in loops', 'While loops', 'String concatenation', 'Casting data types','List comprehension', 'Operators', 'Functions',]
# z = random.choice(py_study)
# y = 0
# study = input('Are you ready to study? ').lower()
# time. sleep(1)
# while y < 1:
#         if study == 'yes':
#                 print('Ok then study:',z)# Fixed: added ",z"  !TODO: this prints every letter on a seperate line, fix it to print all on a single line 1-2-19
#                 y += 1
#         else:
#                 print('Good bye!')
#                 break

