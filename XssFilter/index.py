#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from django import views
from django.shortcuts import render

class Index(views.View):

    def get(self, request):
        return render(request, "index.html")