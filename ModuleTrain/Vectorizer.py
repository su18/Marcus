#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


from sklearn.feature_extraction.text import TfidfVectorizer

import string
import os


class TfIdfVector(TfidfVectorizer):
    """
    TF-IDF向量类
    """
    def __init__(self):
        # tf-idf 向量初始化，截取步长为2Bytes
        super().__init__(smooth_idf=True, use_idf=True, analyzer='char', ngram_range=(2, 2),
                         max_df=0.85, min_df=1, lowercase=False, vocabulary=self.vocabulary_iter())
        self.fit_vector = None
        self.__fit_vector()

    def __fit_vector(self):
        train_sample = []
        current_path = os.path.dirname(os.path.realpath(__file__))
        sample_path = os.path.join(current_path, "train_set\\train.txt")

        # 读取样本
        with open(sample_path, "r", encoding='ISO-8859-1') as file:
            line = file.readline().strip("\r\n")
            while line:
                train_sample.append(line)
                line = file.readline().strip("\r\n")
        self.fit_vector = self.fit_transform(train_sample)

    @staticmethod
    def vocabulary_iter():
        for i in string.printable:
            for j in string.printable:
                yield i + j
