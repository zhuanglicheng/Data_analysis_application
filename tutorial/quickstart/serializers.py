# -*- coding:utf-8 -*-
# 作者：庄立成
# 日期：2020/6/8 14:00
# 工具：PyCharm
# 文件 :serializers.py
# Python版本：3.5.2
from django.contrib.auth.models import User, Group
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')