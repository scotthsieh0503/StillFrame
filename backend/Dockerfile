FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# install chrome
RUN apt-get update
RUN apt-get install -y chromium

COPY . .
EXPOSE 5000
CMD ["flask", "--app", "run"]dpkg -i chromium.deb