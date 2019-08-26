# PyDOODS - Python for Distributed Open Object Detection Service

This is a simple Python wrapper for the [DOODS](https://github.com/snowzach/doods) service. 
DOODS allows you to do remote object detection in images easily. 

A simple example using this library:

```
import PyDOODS from pydoods

try:
    pd = PyDOODS("http://docker:8080",
                    auth_key="abc1234", timeout=5)
except OSError as err:
    print("OS error: {0}".format(err))
    exit
image = open("grace_hopper.png", "rb").read()
print(pd.detect(image))
```
