# Trả lời câu hỏi thảo luận Lab 02

1. **Vì sao phải đồng bộ master trước khi gửi Pull Request?**
   - Trả lời: Trong quá trình phát triển nhánh tính năng, nhánh `master` có thể đã được người khác tích hợp các commit mới. Việc đồng bộ `master` vào nhánh của mình giúp phát hiện và giải quyết xung đột mã nguồn sớm ngay tại máy lập trình viên, đồng thời kiểm thử tích hợp để đảm bảo khi PR được merge sẽ không gây lỗi hệ thống.

2. **Khi nào không được sử dụng rebase?**
   - Trả lời: Tuyệt đối không sử dụng `rebase` trên các nhánh công khai dùng chung (như `master`, `main`, nhánh `release/*`) hoặc các commit đã được push và chia sẻ cho người khác. Bởi vì `rebase` viết lại lịch sử (tạo các mã hash commit mới), sẽ phá vỡ cây lịch sử của các cộng tác viên khác và gây ra lỗi đồng bộ nghiêm trọng.

3. **feature/* khác topic/* ra sao?**
   - Trả lời:
     - `feature/*`: Dùng cho các nhánh phát triển tính năng nghiệp vụ cụ thể của phần mềm (ví dụ: in giỏ hàng, tìm kiếm đĩa).
     - `topic/*`: Dùng cho các nhiệm vụ phi nghiệp vụ nhưng cần thiết cho dự án như cấu hình mẫu PR, viết tài liệu kỹ thuật, nghiên cứu thử nghiệm (Spike).