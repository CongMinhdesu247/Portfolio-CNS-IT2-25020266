# Digital Portfolio Cá Nhân - Hoàng Việt Linh

Dự án Digital Portfolio lưu trữ, hệ thống hóa và trình bày các kết quả học tập thực tế cho học phần **Nhập môn Công nghệ số và Ứng dụng Trí tuệ Nhân tạo (VNU1001)**.

## 📌 Thông tin sinh viên
- **Họ và tên:** Hoàng Việt Linh
- **Mã sinh viên:** 25020234
- **Ngành học:** Công nghệ Thông tin
- **Lớp học:** K70I-IT2
- **Trường:** Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội (UET - VNU)

---

## 📂 Cấu trúc thư mục dự án
Dự án được xây dựng dưới dạng trang web tĩnh, không sử dụng framework:

- `index.html`: Trang chủ giới thiệu bản thân và tổng quan môn học.
- `projects.html`: Bento Grid hiển thị danh sách các bài tập kỹ năng.
- `summary.html`: Trang tổng kết, phản tư và tải tài liệu báo cáo gốc.
- `pages/`: Thư mục chứa các báo cáo chi tiết cho từng bài tập từ Bài 1 đến Bài 7.
- `assets/`: Chứa các tài nguyên tĩnh của trang web:
  - `assets/css/style.css`: Hệ thống CSS responsive & hỗ trợ Dark/Light mode.
  - `assets/js/main.js`: Logic chuyển đổi giao diện và menu điều hướng trên di động.
  - `assets/images/`: Toàn bộ các ảnh minh họa báo cáo và favicon.
- `docs/`: Thư mục chứa các file báo cáo gốc định dạng Word (`.docx`).

---

## ⚡ Các tính năng nổi bật
1. **Thiết kế Bento Grid & Responsive:** Tương thích tốt trên cả máy tính, máy tính bảng và điện thoại di động.
2. **Hỗ trợ Giao diện Sáng/Tối (Dark/Light Mode):** Tự động đồng bộ và lưu trữ lựa chọn của người dùng qua `localStorage`.
3. **Mục lục Động:** Giúp điều hướng nội dung bài viết dài dễ dàng trên thanh sidebar.
