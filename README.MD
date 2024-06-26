# ARTICLE SUMMARIZE

Với Article summarize, bạn có thể tóm tắt nhanh các tin tức nóng nhất trong ngày mà không cần phải đọc quá nhiều nguồn khác nhau. Từ đó, việc nắm bắt các tin tức nóng trong một thời gian ngắn trở nên dễ dàng hơn bao giờ hết.

![Example](screenshots/Demo1.png)

## Công nghệ sử dụng

- Frontend: Vuejs
- Backend: Fastapi

## Mô tả chi tiết
Ở phần giao diện, dự án này chỉ sử dụng Vuejs thuần để làm dự án. Khi người dùng nhập từ khóa vào thanh tìm kiếm, thì nó sẽ gọi đến backend để tìm kiếm thông tin trên Google.

Nhờ vào thư viện yagooglesearch mà ở phía backend có thể search google với nhiều lượt kết quả hơn là thư viện gốc mà google cung cấp. Lý giải tại sao thì có thể xem trên trang của [yagooglesearch](https://pypi.org/project/yagooglesearch/).

Từ kết quả trả về là thông tin và nội dung của các bài báo, backend tiếp tục sử dụng thư viện [underthesea](https://github.com/undertheseanlp/underthesea) để gom nhóm và tách các từ vựng thành từ điển các từ được sử dụng.

Từ các từ vựng đó, backend lại tiếp tục gọi đến thư viện [wordcloud](https://pypi.org/project/wordcloud/) để trực quan hóa các từ vựng có tần suất xuất hiện cao nhất lên.

Cuối cùng, ở phía giao diện sẽ hiển thị hình ảnh các từ vựng được nói đến nhiều nhất và các bài báo mà backend sử dụng để xử lý.

## Môi trường và cài đặt

### Môi trường

Dự án sử dụng:

- Nodejs: 20.10
- Vuejs: 3
- Fastapi: 0.111.0
- Underthesea: 6.8.3
- Wordcloud: 1.9.3
- Matplotlib: 3.9.0
- Python: 3.9.5

### Cài đặt

Mọi người có thể tải dự án về thông qua câu lệnh sau:

``` bash
git clone https://github.com/ltphat2204/article-summarize.git
```

Tiếp đến, tải các thư viện cần thiết cho backend thông qua:

``` bash
cd backend
pip install -r requirements.txt
```

Và run bằng câu lệnh:

``` bash
python main.py
```

Ở Mac hoặc Linux thì sử dụng câu lệnh:

``` bash
python3 main.py
```

Cuối cùng, tải các thư viện cần thiết cho frontend thông qua:

``` bash
cd frontend
npm install
```

Và run bằng câu lệnh:

``` bash
npm run dev
```

Sau khi chạy cả backend lẫn frontend thì bạn có thể truy cập [tại đây](http://localhost:5173/) để xem sản phẩm.
