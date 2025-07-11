 FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
