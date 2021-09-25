import discord
import socket
import threading
import sys
import os
import time


class kommunikation():
  def __init__(self):
    host = "66.11.123.128"
    port = 3746
    buffer = 1024
    sep = "#SEP#"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    enc = encode("UTF-8")
    dec = decode("UTF-8")
    self.s = s
    self.host = host
    self.port = port
    self.buffer = buffer
    self.sep = sep

  def verbinden(self, args):
    self.s.connect((self.host, self.port))
    self.s.send(sys.args[1].enc())
    self.s.close()
