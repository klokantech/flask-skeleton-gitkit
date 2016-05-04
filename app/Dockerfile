FROM debian:8
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8000

# Uncomment if you need an entrypoint.
# ENTRYPOINT ["/venv/entrypoint.sh"]

RUN apt-get -qq update && apt-get -qq -y --no-install-recommends install \
    build-essential \
    ca-certificates \
    gettext \
    libffi-dev \
    libpq-dev \
    python3 \
    python3-dev \
    python3-venv

COPY requirements.txt /venv/requirements.txt
RUN python3 -m venv /venv \
&& /venv/bin/pip install -r /venv/requirements.txt \
&& /venv/bin/pip freeze > /venv/requirements-freezed.txt

# Uncomment if you need an entrypoint.
# COPY entrypoint.sh /venv/entrypoint.sh

ARG PACKAGE_NAME
ARG PACKAGE_VERSION
ENV PACKAGE_NAME=$PACKAGE_NAME
ENV PACKAGE_VERSION=$PACKAGE_VERSION

COPY . /venv/app

ARG SETUP_MODE
RUN /venv/app/setup.sh $SETUP_MODE
