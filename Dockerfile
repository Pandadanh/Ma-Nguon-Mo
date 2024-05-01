# Sử dụng image Python chính thức
FROM python:3.8
# Copy các file yêu cầu
COPY requirements.txt .

# Cài đặt các thư viện
RUN pip install -r requirements.txt

# Copy toàn bộ code vào trong container
COPY . .

# Thiết lập cổng mạng container sử dụng
EXPOSE 8000

# Lệnh để chạy ứng dụng Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
