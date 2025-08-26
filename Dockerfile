FROM python:3.9-slim 
# Set working directory inside container
WORKDIR /app
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .
ENTRYPOINT [ "streamlit" , "run" ]
CMD [ "main.py" ]
