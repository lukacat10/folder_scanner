FROM python:3

COPY . .

RUN python -m pip install -e .

CMD [ "folder_scanner" ]