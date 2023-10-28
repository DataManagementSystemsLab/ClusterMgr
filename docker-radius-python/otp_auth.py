#! /usr/bin/env python3
import radiusd
import sys
import db_access as dba
import utils
# Check post_auth for the most complete example using different
# input and output formats
cnx=None

def instantiate0(p):
  print("*** instantiate ***")
  print(p)
  return 0

def authorize0(p):
  print("*** authorize 2.***")
  
  return  (radiusd.RLM_MODULE_UPDATED, (), (('Auth-Type','Accept'),))

def authenticate(p):
    print(p)
    p["config"]=(("Auth-Type","Accept"))
    return radiusd.RLM_MODULE_OK, p

def instantiate(p):
  print("*** instantiate ***")
  print(p)
  #cnx=dba.connect()
  return 0

def authorize(p):
  print("*** authorize 3.***")
  #print(p)
  d=dict(p)
  print(d)
  cnx=dba.connect()
  print(cnx)

  ac,reply=  utils.check_authorize(cnx,d)
  print ("reply")
  print(reply)
  print (ac)
  if ac:
    return  (radiusd.RLM_MODULE_UPDATED,(), (('Auth-Type', 'Accept'),))
 
  return (radiusd.RLM_MODULE_REJECT, (('Reply-Message', 'Code is not valid'),),(('Auth-Type','Reject'),)) 

def preacct(p):
  print("*** preacct ****")
  print(p)
  return radiusd.RLM_MODULE_OK

def accounting(p):
  print("*** accounting ***")
  radiusd.radlog(radiusd.L_INFO, '*** radlog call in accounting (0) ***')
  print()
  print(p)
  return radiusd.RLM_MODULE_OK

def pre_proxy(p):
  print("*** pre_proxy ***")
  print(p)
  return radiusd.RLM_MODULE_OK

def post_proxy(p):
  print("*** post_proxy ***")
  print(p)
  return radiusd.RLM_MODULE_OK

def post_auth(p):
  print("*** post_auth ***")
  # This is true when using pass_all_vps_dict
  print(p)
  # Dictionary representing changes we want to make to the different VPS
  update_dict = {
        "request": (("User-Password", ":=", "A new password"),),
        "reply": (("Reply-Message", "The module is doing its job"),
                  ("User-Name", "NewUserName")),
        "config": (("Cleartext-Password", "A new password"),),
  }

  return radiusd.RLM_MODULE_UPDATED, update_dict
  # Alternatively, you could use the legacy 3-tuple output
  # (only reply and config can be updated)
  # return radiusd.RLM_MODULE_OK, update_dict["reply"], update_dict["config"]

def recv_coa(p):
  print("*** recv_coa ***")
  print(p)
  return radiusd.RLM_MODULE_OK

def send_coa(p):
  print("*** send_coa ***")
  print(p)
  return radiusd.RLM_MODULE_OK

def detach(p):
  print("*** goodbye from example.py ***")
  cnx.close()
  return radiusd.RLM_MODULE_OK
