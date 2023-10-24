try:
    x = int ("Hello World")
except:
    print("There was an error")
else: 
    print("There was no exception")
finally:
    print("This will happen every time")