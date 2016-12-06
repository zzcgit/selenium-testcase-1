FROM registry.aliyuncs.com/acs-sample/python:2.7
RUN pip install selenium nose
COPY samp-login-search.py .
CMD ["sh", "-c", "sleep 15 && nosetests"]
