# Trả lời câu hỏi thảo luận Lab 03

1. **Merge base là gì?**
   - Trả lời: Merge base là commit tổ tiên chung gần nhất (best common ancestor) giữa hai nhánh đang được thực hiện hòa trộn. Git dựa vào merge base để so sánh sự khác biệt giữa hai nhánh và thực hiện thuật toán hòa trộn 3 bên (3-way merge).

2. **Vì sao trên master và release/* phải dùng git revert thay vì git reset?**
   - Trả lời: Nhánh `master` và `release/*` là các nhánh công khai đã được chia sẻ cho cả nhóm và hệ thống CI/CD. Lệnh `git reset` xóa bỏ các commit khỏi lịch sử và bắt buộc phải dùng `force push`, làm mất tính toàn vẹn của lịch sử và làm hỏng repo cục bộ của người khác. Trong khi đó, `git revert` tạo một commit mới với nội dung đảo ngược lại thay đổi trước đó, giúp giữ nguyên vẹn toàn bộ tiến trình lịch sử để phục vụ mục đích kiểm toán (audit).

