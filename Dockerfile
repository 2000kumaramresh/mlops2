FROM python:3.9.17
COPY . /digits/
RUN pip3 install --no-cache-dir -r /digits/requirements.txt
WORKDIR /digits
RUN python3 exp.py

ENV FLASK_APP =app.py
CMD ["flask", "run"]