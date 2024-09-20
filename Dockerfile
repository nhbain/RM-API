FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY ./lambda/hello_rm_app.py "${LAMBDA_TASK_ROOT}"/hello_rm_app.py

CMD [ "hello_rm_app.handler" ]
