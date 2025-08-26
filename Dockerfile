FROM python:3.9-slim 
WORKDIR /app COPY main.py /app/
COPY requirements.txt /app/ 
COPY best_gradient_boosting_model.pkl /app/ 
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "streamlit" , "run" ] CMD [ "main.py" ]