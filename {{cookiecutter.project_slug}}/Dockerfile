FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Setup working directory
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt


# Setup Postgres
RUN apt update && apt install -y lsb-release && apt clean all
RUN wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | tee  /etc/apt/sources.list.d/pgdg.list
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg-testing main 13" | tee  /etc/apt/sources.list.d/pgdg-testing.list
RUN apt-get -y update && apt-get -y upgrade
RUN apt -y --fix-missing install postgresql-client-13


COPY . /code/

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["sh", "/code/entrypoint.sh"]