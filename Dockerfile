FROM python:3.8-slim as prod
ARG DISCORD_ARG
ENV DISCORD_TOKEN=$DISCORD_ARG

COPY / /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ADD start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "/start.sh"]