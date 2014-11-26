#!/usr/bin/python

import requests

def func_a():
    return 3

def func_b(a):
    return a+2

def func_c(a,b):
    return a if b > 10 else b

def func_d():
    r = requests.get('https://google.com')
    if r.status_code == 200:
        return 1
    elif r.status_code == 404:
        return 2
    else:
        return 3

def func_e():
    r = requests.get('https://google.com')
    if r.status_code >= 400:
        raise Exception('Error')
    return 1
