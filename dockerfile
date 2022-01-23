#base image
FROM python
COPY . /cloud_assignment1
WORKDIR /cloud_assignment1
RUN pip install numpy
RUN pip install nltk
CMD python pyfile.py
