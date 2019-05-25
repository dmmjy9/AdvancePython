try:
    print("code started")
    raise KeyError
except KeyError as e:
    print("key error")
else:
    print("other error")
finally:
    print("finally")
