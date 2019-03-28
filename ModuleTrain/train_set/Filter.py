#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import re


def xss_filter(string):
    rule0 = "Your XSS Rule Here"
    rule1 = "Your XSS Rule Here"
    rule2 = "Your XSS Rule Here"
    rule3 = "Your XSS Rule Here"
    rule4 = "Your XSS Rule Here"
    rule5 = "Your XSS Rule Here"
    rule6 = "Your XSS Rule Here"
    rule7 = "Your XSS Rule Here"
    rule8 = "Your XSS Rule Here"
    rule9 = "Your XSS Rule Here"

    rule = [rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]
    for i in rule:
        a = re.match(i, string)
        if a:
            return True
    return False
