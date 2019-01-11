#! /usr/bin/env python
# coding:utf-8

import poplib

host = "pop3.126.com"
port = 22

pop3 = poplib.POP3_SSL(host, port )