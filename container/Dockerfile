FROM alpine:3.16
RUN apk add --no-cache \
    python3 \
    py3-pip \
    git \
    npm

RUN mkdir /home/web_app
RUN git clone https://github.com/cdtx/cyrildutrieux.net /home/web_app
RUN pip3 install -r /home/web_app/requirements.txt
RUN pip install /home/web_app
 
RUN git clone https://github.com/cdtx/django_error_handlers.git /tmp/django_error_handlers
RUN pip3 install /tmp/django_error_handlers
RUN rm -rf /tmp/django_error_handlers
 
RUN git clone https://github.com/cdtx/easy_password.git /tmp/easy_password
RUN pip3 install /tmp/easy_password
RUN rm -rf /tmp/easy_password

# Install node packages
WORKDIR /home/web_app/project/assets
RUN npm install 

WORKDIR /home/web_app/project

COPY config.ini config.ini
RUN ln -s /volume/db.sqlite3 db.sqlite3
RUN python3 manage.py collectstatic

# Collect static

