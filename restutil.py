# Copyright 2014 NeuroData (http://neurodata.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import requests
try:
  from django.conf import settings
  SECRET_TOKEN = settings.SECRET_TOKEN
except:
  SECRET_TOKEN = None

#def getURL(url):
  #"""Fetch a URL"""

  #try:
    #req = urllib2.Request(url)
    #resp = urllib2.urlopen(req)
    #return resp.read()
  #except urllib2.URLError as e:
    #print "Failed URL {}. Error {}".format(url, e)
    #raise e


# def getURLTimed(url):
  # """Fetch a URL"""

  # try:
    # req = urllib.request.Request(url)
    # start = time.time()
    # resp = urllib.request.urlopen(req)
  # except urllib.error.URLError as e:
    # raise

#def putURL(url, data):
  #"""Post a URL"""

  #try:
    #req = urllib2.Request(url, data)
    #resp = urllib2.urlopen(req)
  #except urllib2.URLError as e:
    #print "Failed URL {}. Error {}".format(url, e)


# def putURLTimed(xxx_todo_changeme):
  # """Post a URL"""
  # (url, data) = xxx_todo_changeme
  # try:
    # req = urllib.request.Request(url, data)
    # start = time.time()
    # resp = urllib.request.urlopen(req)
  # except urllib.error.URLError as e:
    # raise

def generateURLBlosc(server_name, token_name, channel_list, res_value, range_args):
  """Generate a URL for blosc"""

  try:
    url = "http://{}/ca/{}/{}/blosc/{}/{},{}/{},{}/{},{}/".format(server_name, token_name, ','.join(channel_list), res_value, *range_args)
  except Exception as e:
    return ""

  return url


def generateURLBlaze(server_name, token_name, channel_list, res_value, range_args):
  """Generate a URL for blosc"""

  try:
    url = "http://{}/blaze/{}/{}/blosc/{}/{},{}/{},{}/{},{}/".format(server_name, token_name, ','.join(channel_list), res_value, *range_args)
  except Exception as e:
    return ""

  return url

def postJson(url, data):

  try:
    response = requests.post(url, json=data, headers={'Authorization': 'Token {}'.format(SECRET_TOKEN)} if SECRET_TOKEN else None, verify=False)
    return response
  except requests.HTTPError as e:
    return e

def getJson(url):
  return getURL(url)

def deleteJson(url):
  return deleteURL(url)

def getURL(url):
  try:
    response = requests.get(url, headers={'Authorization': 'Token {}'.format(SECRET_TOKEN)} if SECRET_TOKEN else None, verify=False)
    return response
  except requests.HTTPError as e:
    return e

def deleteURL(url):
  try:
    response = requests.delete(url, headers={'Authorization': 'Token {}'.format(SECRET_TOKEN)} if SECRET_TOKEN else None, verify=False)
    return response
  except requests.HTTPError as e:
    return e

def postURL(url, data):
  try:
    response = requests.post(url, data, headers={'Authorization': 'Token {}'.format(SECRET_TOKEN)} if SECRET_TOKEN else None, verify=False)
    return response
  except requests.HTTPError as e:
    return e
