#!/usr/bin/python
# coding: utf-8

from ConfigParser import ConfigParser
import os

web_root = os.path.abspath(".")
config_path = os.path.join(web_root, "config")

cp = ConfigParser()
cp.read(os.path.join(config_path, "config.ini"))
user = dict(cp.items("user"))
