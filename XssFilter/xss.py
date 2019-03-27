#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from django import views
from django.shortcuts import HttpResponse
import json
from ModuleTrain.Detector import Detector


class XssDetect(views.View):

    def post(self, request):
        string = request.POST.get('string', None)
        xss = Detector(input_string=string)
        result = xss.xss_predict()
        print(result)
        if result == [-1]:
            return self.http_response(status='false', message='正常行为', data=string)
        elif result == [1]:
            return self.http_response(status='true', message='检测到XSS攻击', data='')

    @staticmethod
    def http_response(status, message, data):
        """
        使用HttpResponse返回JSON格式数据
        :param status:
        :param message:
        :param data:
        :return:
        """
        return_data = {'status': status, 'message': message, 'data': data}
        return HttpResponse(json.dumps(return_data, ensure_ascii=False, indent=4),
                            content_type='application/json',
                            charset='utf-8')