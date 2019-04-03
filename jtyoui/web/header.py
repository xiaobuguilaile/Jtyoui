#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time : 2019/2/19 0019
# @Email : jtyoui@qq.com


def header(request_headers):
    """
    将浏览器中的Request Headers头复制过来.进行改装成字典类型
    :param request_headers:  浏览器中的Request Headers头信息
    :return: 分割Headers头信息的键值对
    """
    headers = dict()
    for head in request_headers.rsplit('\n'):
        name, values = head.split(':', 1)
        headers[name] = values.strip(' ')
    return headers


Response_Headers = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-language: zh-CN,zh;q=0.9,en;q=0.8
cache-control: max-age=0
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"""

free_header = header(Response_Headers)

if __name__ == '__main__':
    print(header(Response_Headers))
