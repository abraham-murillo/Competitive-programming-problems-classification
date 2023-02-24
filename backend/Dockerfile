# FROM python:3.9-alpine
FROM python:3.10-bullseye

ENV path="/Competitive-programming-problems-classification/backend/"

WORKDIR /idk

COPY requirementsMacbook.txt requirements.txt 

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install python-dotenv
RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]

CMD ["python3", "api.py"]