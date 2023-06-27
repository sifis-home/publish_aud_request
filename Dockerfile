FROM python:3.7.6
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN pip install websocket-client
RUN pip install rel
RUN pip install requests

WORKDIR /publish_aud_request
COPY publish_aud_request.py /publish_aud_request

# Install Docker from Docker Inc. repositories.
# RUN curl -sSL https://get.docker.com/ | sh

CMD ["python", "publish_aud_request.py"]