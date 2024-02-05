FROM python:3.10.13-slim

WORKDIR /usr/app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends tzdata lsb-release curl gpg\
	&& curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg\
	&& echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list\
	&& apt-get install -y --no-install-recommends redis\	
	&& apt-get clean \
	&& rm -rf /var/lib/apt-get/lists/* /tmp/* /var/tmp/*
RUN service redis-server start

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

EXPOSE 6379 8000
CMD ["python3", "app.py"]
