FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# install chrome
RUN apt-get update
RUN apt-get install libpci3 libx11-dev libgtk-3-0 libdbus-1-3 libegl1-mesa libgles2-mesa xvfb firefox-esr -y

COPY . .
EXPOSE 5000
CMD ["flask", "--app", "run"]