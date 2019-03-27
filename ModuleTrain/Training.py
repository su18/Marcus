#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


import os
from sklearn.svm import OneClassSVM
from ModuleTrain.Vectorizer import TfIdfVector
from datetime import datetime
import numpy as np
from sklearn.model_selection import ParameterGrid
import pickle


class Train:
    def __init__(self, path=None):
        self.root_path = path
        self.set_path = os.path.join(self.root_path, "ModuleTrain/train_set/")
        self.train_path = os.path.join(self.root_path, "ModuleTrain/train_set/train.txt")
        self.test_none_xss_path = os.path.join(self.root_path, "ModuleTrain/train_set/none_xss.txt")
        self.test_xss_path = os.path.join(self.root_path, "ModuleTrain/train_set/xss.txt")
        self.complete = False

    def is_complete(self):
        return self.complete

    def set_complete(self, v: bool):
        self.complete = v

    @staticmethod
    def read_txt(path: str, l: list, encoding='ISO-8859-1'):
        with open(path, "r", encoding=encoding) as file:
            print(path)
            line = file.readline().strip("\r\n")
            while line:
                l.append(line)
                line = file.readline().strip("\r\n")

    def get_model(self):
        start = datetime.now()
        print("Start at {}".format(start.strftime("%Y/%m/%d %H:%M:%S")))
        train_example = []
        xss_example = []
        non_xss_example = []

        # 读取训练集(整理好的XSS Payload)
        self.read_txt(self.train_path, train_example)
        # 读取正常请求样本集
        self.read_txt(self.test_none_xss_path, non_xss_example)
        # 读取攻击请求样本集
        self.read_txt(self.test_xss_path, xss_example)
        # 特征向量化训练样本
        tf_idf_vector = TfIdfVector()
        train_vector = tf_idf_vector.fit_vector
        # 特征向量化黑白样本
        test_normal_vector = tf_idf_vector.transform(xss_example)
        test_abnormal_vector = tf_idf_vector.transform(non_xss_example)
        y = [1] * (len(train_example))
        #  遍历调优参数nu与gamma
        grid = {'gamma': np.logspace(-8, 1, 10),
                'nu': np.linspace(0.01, 0.20, 20)}
        # 核函数(rbf,linear,poly)
        kernel = 'rbf'
        # 最高准确度、召回率、F1值纪录
        max_F1 = 0
        max_Re = 0
        max_Pr = 0
        # 最高准确度、召回率、F1值时参数gamma的值
        gamma_r_F1 = 0.01
        gamma_r_Re = 0.01
        gamma_r_Pr = 0.01
        # 最高准确度、召回率、F1值时参数nu的值
        nu_r_F1 = 0
        nu_r_Re = 0
        nu_r_Pr = 0
        svdd = OneClassSVM(kernel=kernel)
        zero_count = 0
        re_gamma = 0
        total_loop = len(ParameterGrid(grid))
        process_count = 0
        for z in ParameterGrid(grid):
            process_count += 1
            if re_gamma == z.get('gamma'):
                if zero_count >= 4:
                    continue
            else:
                zero_count = 0
            svdd.set_params(**z)
            svdd.fit(train_vector, y)
            k = svdd.get_params()

            # 攻击请求样本测试
            f = svdd.predict(test_normal_vector)
            TP = f.tolist().count(1)  # True positive
            FN = f.tolist().count(-1)  # False Negative

            # 非攻击样本测试
            f = svdd.predict(test_abnormal_vector)
            FP = f.tolist().count(1)  # False positive
            Precision = 0 if TP == 0 else (TP / (TP + FP))  # Precision
            Recall = 0 if TP == 0 else (TP / (TP + FN))  # Recall
            if Recall == 0 or Precision == 0:
                F1_score = 0
                zero_count += 1
                re_gamma = k.get('gamma')
            else:
                F1_score = 2 * Precision * Recall / (Precision + Recall)  # F1 value

            if F1_score > max_F1:
                max_F1 = F1_score
                nu_r_F1 = k.get('nu')
                gamma_r_F1 = k.get('gamma')

            if Recall > max_Re:
                max_Re = Recall
                nu_r_Re = k.get('nu')
                gamma_r_Re = k.get('gamma')

            if Precision > max_Pr:
                max_Pr = Precision
                nu_r_Pr = k.get('nu')
                gamma_r_Pr = k.get('gamma')

            print("========================== [{}] ===========================".format(
                    datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
            print("nu: ", k.get('nu'), 'gamma', k.get('gamma'), )
            print("Precision: {}%".format(Precision * 100))
            print("Recall: {}%".format(Recall * 100))
            print("F1 score: {}".format(F1_score))
        print("========================== [{}] ===========================".format(
                datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

        print("MAX Precision:  {:^20.6f}When Current nu: {:^20.6f} and gamma: {:0.8f}".format(max_Pr, nu_r_Pr,
                                                                                              gamma_r_Pr))
        print("MAX Recall:     {:^20.6f}When Current nu: {:^20.6f} and gamma: {:0.8f}".format(max_Re, nu_r_Re,
                                                                                              gamma_r_Re))
        print("MAX F1:         {:^20.6f}When Current nu: {:^20.6f} and gamma: {:0.8f}".format(max_F1, nu_r_F1,
                                                                                              gamma_r_F1))
        total_second = datetime.now() - start
        print("Cost {}s.".format(total_second.total_seconds()))
        with open(os.path.join(self.root_path, "ModuleTrain/cache/model.pkl"), 'wb') as file:
            svdd.set_params(kernel=kernel, nu=nu_r_F1, gamma=gamma_r_F1)
            svdd.fit(train_vector, y)
            pickle.dump(svdd, file)
        self.complete = True


if __name__ == '__main__':
    train1 = Train(path="E:\PY-Study\XssFilter")
    train1.get_model()
