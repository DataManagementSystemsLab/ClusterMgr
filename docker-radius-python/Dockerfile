# Use Base Ubuntu image
FROM ubuntu:22.04
# Author of this Dockerfile
# MK <mohamedkhalefa@gmail.com>
# Update & upgrades
RUN apt-get update && apt-get dist-upgrade -y
# Install FreeRADIUS and Google Authenticator
RUN apt-get install freeradius freeradius-python3 python3 python3-pip  rsyslog -y

# Clear local repo
RUN pip3 install pyotp  mysql-connector-python qrcode Pillow   
RUN pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

#RUN apt-get remove python3-pip
RUN apt-get clean

# Edit /etc/freeradius/3.0/mods-config/files/authorize file
# This is the real file for /etc/freeradius/3.0/users
# Copy existing /etc/freeradius/sites-available/default file to container
# This is the real file for /etc/freeradius/3.0/sites-enabled/default

RUN rm  -f /etc/freeradius/3.0/sites-available/default || true
RUN rm -f  /etc/freeradius/3.0/clients.conf || true
RUN rm -f   /etc/freeradius/3.0/mods-config/python3/otp_auth.py || true
RUN rm -f /etc/freeradius/3.0/mods-available/python3 || true
COPY python3.mod /etc/freeradius/3.0/mods-available/python3
COPY default /etc/freeradius/3.0/sites-available/default
COPY clients.conf /etc/freeradius/3.0/clients.conf
COPY otp_auth.py  /etc/freeradius/3.0/mods-config/python3/otp_auth.py
COPY db_access.py  /etc/freeradius/3.0/mods-config/python3/db_access.py
COPY utils.py  /etc/freeradius/3.0/mods-config/python3/utils.py


#COPY authorize /etc/freeradius/3.0/mods-config/files/authorize
# Create a symbolic link
RUN ln -s /etc/freeradius/3.0/mods-available/python3 /etc/freeradius/3.0/mods-enabled/python3

# Change owner of the directory to freerad
RUN chown freerad:freerad /etc/freeradius/3.0/mods-config/python3/otp_auth.py
RUN chown freerad:freerad /etc/freeradius/3.0/mods-available/python3
RUN chown freerad:freerad /etc/freeradius/3.0/clients.conf
RUN chown freerad:freerad /etc/freeradius/3.0/sites-available/default
#RUN chown freerad:freerad /etc/freeradius/3.0/mods-config/files/authorize
# Copy .google_authenticator file to /etc/freeradius/networkjutsu

EXPOSE 1812/udp 1813/udp 18120/udp
# Run FreeRADIUS as a foreground process
CMD ["freeradius","-X"]
