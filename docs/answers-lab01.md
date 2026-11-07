# Trả lời câu hỏi thảo luận Lab 01

1. **Vì sao dùng git mv thay vì di chuyển tệp bằng hệ điều hành thông thường?**
   - Trả lời: `git mv` thông báo trực tiếp cho Git rằng đây là thao tác di chuyển/đổi tên tệp. Điều này giúp Git tự động đánh dấu tệp ở trạng thái `renamed` trong Staging Area và bảo toàn toàn bộ lịch sử commit trước đó của tệp. Nếu dùng lệnh di chuyển thông thường của hệ điều hành, Git sẽ coi đó là 2 thao tác độc lập (xóa tệp cũ và tạo một tệp mới tinh), làm đứt gãy tính liên tục của lịch sử theo dõi (trừ khi dùng thuật toán phỏng đoán tương đồng nội dung).

2. **release/lab01 có phải là một baseline không?**
   - Trả lời: Có. `release/lab01` đóng vai trò là một baseline trong quy trình SCM. Nó biểu diễn một trạng thái cấu hình phần mềm đã được kiểm tra, nghiệm thu và thống nhất đóng băng tại thời điểm hoàn thành Lab 01 để làm cơ sở đánh giá bài nộp. Mọi thay đổi tiếp theo của dự án sẽ không được ghi đè trực tiếp lên nhánh này.

3. **Vì sao không commit thẳng lên master dù chỉ làm việc một mình?**
   - Trả lời: Nhánh `master` đại diện cho mã nguồn ổn định nhất sẵn sàng triển khai. Việc tuân thủ quy trình tạo nhánh riêng và mở PR dù làm một mình đem lại các lợi ích SCM:
     - Cho phép tự rà soát (self-review) toàn bộ diff trước khi mã được hòa trộn.
     - Tạo ra một điểm ghi nhận lịch sử (audit trail) rõ ràng gắn với từng mục đích cụ thể.
     - Rèn luyện kỷ luật quy trình chuẩn xác giống như làm việc trong môi trường nhóm thực tế.