# Trả lời câu hỏi thảo luận Lab 04

1. **Vì sao nhánh release/* không bao giờ merge ngược vào master?**
   - Trả lời: Nhánh `release/*` đại diện cho một phiên bản phát hành cụ thể đã được đóng băng để chuyển giao. Nhánh này chỉ tồn tại để nhận các bản sửa lỗi khẩn cấp (hotfix). Nếu có hotfix trên release, các commit sửa lỗi đó sẽ được đưa về master bằng lệnh `git cherry-pick`, tuyệt đối không merge toàn bộ nhánh release vào master để tránh kéo theo các thay đổi cấu hình đặc thù của phiên bản cũ làm ghi đè hoặc sai lệch nhánh master đang phát triển bản cao hơn.

2. **So sánh Release Flow với GitFlow:**
   - Trả lời:
     - *GitFlow:* Phức tạp với hai nhánh tồn tại song song vĩnh viễn là `develop` và `master`, đòi hỏi merge qua lại nhiều bước, dễ dẫn đến tình trạng "merge hell" khi quy mô dự án mở rộng.
     - *Release Flow:* Đơn giản, tinh gọn hơn với chỉ một nhánh chính duy nhất là `master`. Các nhánh tính năng sống ngắn được merge liên tục vào master. Nhánh release chỉ được tách ra khi đến mốc bàn giao và không merge ngược về master, giúp kiểm soát phiên bản linh hoạt và phù hợp với mô hình CI/CD hiện đại.

3. **Vì sao nâng phiên bản lên 1.0.0 mà không phải 0.4.0?**
   - Trả lời: Theo quy tắc Semantic Versioning, dải phiên bản `0.y.z` là giai đoạn phát triển ban đầu, API và tính năng chưa ổn định. Việc chuyển sang phiên bản `1.0.0` đánh dấu một mốc quan trọng: phần mềm đã hoàn thiện toàn bộ các tính năng cốt lõi đầu tiên, đạt độ ổn định cao và sẵn sàng đưa vào môi trường sản xuất để người dùng sử dụng.

