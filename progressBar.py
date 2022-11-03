# Attach your progress bar into your application to make beautful effect for better user experience


# Type: 1 Without using any external libraries-------------- 
# Note: If you are using colorama then please use intelligent terminals like linux, pycharm, jupiter NB, VScode and not CMD
import colorama

def progressBar(progress, total, color = colorama.Fore.GREEN):
    prct = 100 * (progress / float(total))
    bar = '█' * int(prct) + ' ' * (100 - int(prct))
    print(color + f'\r{bar}| Status: {prct:.2f} %', end='\r')



## -----------EXAMPLE for using progress Bar------------
import math
num = [x*5 for x in range(2000, 3000)]
res =[]
progressBar(0, len(num))
for i, v in enumerate(num):
    res.append(math.factorial(v))
    progressBar(i+1, len(num))



print(colorama.Fore.RESET)
## # Type: 2 using  external libraries (Pandas datareader)-------------- 

# import pandas_datareader as pdt

