# Trả lời câu hỏi thảo luận Lab 05

1. **Ưu, nhược điểm của chính sách "upstream first" so với "release first"?**
   - Trả lời:
     - *Upstream first (Sửa lỗi trên master trước rồi cherry-pick về release):*
       - Ưu điểm: Đảm bảo lỗi không bao giờ bị quên sửa trên nhánh chính, tránh việc các phiên bản tương lai bị lặp lại lỗi cũ (regression).
       - Nhược điểm: Khó khăn nếu mã nguồn trên master đã thay đổi quá nhiều so với bản release, việc cherry-pick ngược về bản cũ có thể gặp xung đột lớn.
     - *Release first (Sửa lỗi trên nhánh release trước rồi lan truyền về master):*
       - Ưu điểm: Khắc phục sự cố cho khách hàng nhanh nhất, kiểm thử trực tiếp trên chính môi trường mà khách hàng đang gặp lỗi.
       - Nhược điểm: Lập trình viên rất dễ quên lan truyền bản sửa về master, dẫn đến việc lỗi tái xuất hiện ở các bản phát hành sau.

2. **Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?**
   - Trả lời: Lệnh `git cherry -v origin/release/lab05 origin/release/lab04` sẽ liệt kê các commit có trên nhánh release/lab04 nhưng chưa có trên release/lab05 (ký hiệu dấu `+`). Hoặc vòng lặp chạy test tự động trên tất cả các ref phiên bản:
     ```bash
     for ref in v1.0.1 v1.1.0 master; do
       git switch --detach -q $ref
       python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
     done
     ```
     sẽ chỉ ra ngay phiên bản nào không vượt qua được kiểm thử (trả về kết quả `0` thay vì `1`).

