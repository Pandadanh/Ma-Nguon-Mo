# Sử dụng image Python chính thức
FROM python:3.8

# Copy các file yêu cầu
COPY requirements.txt .

# Cài đặt các thư viện
RUN pip install -r requirements.txt

# Copy toàn bộ code vào trong container
COPY . .

# Thiết lập cổng mạng container sử dụng
EXPOSE 8070

# Lệnh để chạy ứng dụng FastAPI
CMD ["uvicorn", "lyric:app", "--host", "0.0.0.0", "--port", "8070", "--reload"]

