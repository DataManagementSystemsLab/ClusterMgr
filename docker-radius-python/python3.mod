python3 {
    

  python_path = ${modconfdir}/${.:name}:/usr/local/lib/python3.10/dist-packages
  module = otp_auth

  
 mod_instantiate  = ${.module}
   func_instantiate = instantiate
 
 mod_authorize = ${.module}
  func_authorize = authorize

 # mod_authenticate = ${.module}
 # func_authenticate = authenticate


 # mod_post_auth = ${.module}
  #func_post_auth = post_auth
}
