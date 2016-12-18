#todo base on compiled pdf2html version
FROM bwits/pdf2htmlex

RUN apt-get update && apt-get install -y python3-pip locales
RUN apt-get install -y libssl-dev
#RUN locale-gen en_US.UTF-8
COPY requirements.txt /pdf/
RUN pip3 install -r requirements.txt
COPY . /pdf
ENV PYTHONIOENCODING UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
ENV FLASK_APP web.py
ENV FLASK_DEBUG 1

CMD python3 web.py
