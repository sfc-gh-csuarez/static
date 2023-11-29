   
FROM python:3.9-slim
WORKDIR /app
RUN pip install snowflake-snowpark-python && \
    pip install streamlit && \
    pip install langchain && \
    pip install openai
COPY home.py /app
COPY pages /app/pages
COPY templates/index.html ./templates/index.html
EXPOSE 8001
ENTRYPOINT ["streamlit","run","home.py","--server.port=8001", "--server.address=0.0.0.0"]