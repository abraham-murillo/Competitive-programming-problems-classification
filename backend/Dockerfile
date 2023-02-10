FROM anibali/pytorch:cuda-10.0

ENV path=/Competitive-programming-problems-classification/backend/

WORKDIR ${path}

RUN sudo apt-get update
RUN sudo apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
RUN pip3 install -r ./requirementsMacbook.txt

COPY . ${path}
RUN sudo chmod -R a+rwx ${path}
CMD ["python3", "api.py"]~