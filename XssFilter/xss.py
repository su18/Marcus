#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from django import views
from django.shortcuts import HttpResponse
import json
import string
from ModuleTrain.Detector import Detector
from ModuleTrain.train_set.Filter import xss_filter


class XssDetect(views.View):

    def post(self, request):
        # 获取用户传递字符串
        post_string = request.POST.get('string', None)

        # 开启和关闭XSS防御
        flag = True
        #flag = False

        if flag:
            if len(post_string) < 60:
                new_string = post_string.lower().replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "").replace("\0", "").strip()
                if new_string in string.printable:
                    return self.http_response(status=False, message='正常行为', data=post_string)
                else:
                    if xss_filter(new_string):
                        # print("rule detect:"+string)
                        return self.http_response(status=True, message='检测到XSS攻击', data='')
                    else:
                        # 使用模型预测结果
                        xss = Detector(input_string=new_string)
                        result = xss.xss_predict()
                        if result == [-1]:
                            with open('E:/Project/Github/Marcus-XssFilter/Marcus/ModuleTrain/train_set/bypass.txt', 'w+') as file:
                                file.write("Bypass:" + post_string + '\n')
                            return self.http_response(status=False, message='正常行为', data=post_string)
                        elif result == [1]:
                            # print("algorithm detect:" + string)
                            return self.http_response(status=True, message='检测到XSS攻击', data='')
            else:
                return self.http_response(status=True, message='参数过长', data='')
        else:
            return self.http_response(status=False, message='正常行为', data=post_string)

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