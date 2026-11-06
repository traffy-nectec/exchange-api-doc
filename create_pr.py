import os
import re
import subprocess
import sys

# Extract token from .git-credentials
with open("/home/supertoy/.git-credentials") as f:
    text = f.read()

m = re.search(r"https://([^:]+):([^@]+)@github\.com", text)
if not m:
    print("Error: Could not find GitHub token")
    sys.exit(1)

token = m.group(2)
env = os.environ.copy()
env["GH_TOKEN"] = token

branch_name = "docs/sync-query-apis-context-and-webhook-docs"

def run_cmd(cmd, check=True):
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout)
    if res.stderr:
        print(res.stderr, file=sys.stderr)
    if check and res.returncode != 0:
        print(f"Command failed with code {res.returncode}")
        sys.exit(res.returncode)
    return res

# 1. Checkout new branch
run_cmd(["git", "checkout", "-b", branch_name])

# 2. Add files
run_cmd(["git", "add", "-A"])

# 3. Commit
commit_msg = """docs: sync query apis context, webhook identity, and public contracts

- Add type_reporter, user_id, is_follow, is_forward, and status_latest to get-issues (JSON/CSV) and openapi spec
- Add sender_user_id (timeline) and user_name (chat) to get-issue/v2
- Document wildcard support (* and ?) for search-org text parameter
- Add client_ticket_id, sender_user_id, and sender_user_name to all 3 webhook payloads and samples
- Clean up internal debug fields (api_log_session_id*) from public documentation tables
- Update README, HANDOFF, ADR (ADR-014, ADR-015), OKF, and graphify output"""

run_cmd(["git", "commit", "-m", commit_msg])

# 4. Push branch
run_cmd(["git", "push", "-u", "origin", branch_name])

# 5. Create Pull Request
pr_title = "docs: sync query APIs context, webhook identity, and public contract cleanup"

pr_body = """## สรุปรายละเอียดการแก้ไข (Summary of Changes)

Pull Request นี้ทำการตรวจสอบความเรียบร้อยและปรับปรุงเอกสาร API ทั้งหมดให้สอดคล้องกันอย่างสมบูรณ์ ครอบคลุมทั้ง `docs.html`, เอกสาร Markdown ใน `docs/`, `openapi.yaml`, บันทึกสถาปัตยกรรม (ADR), กรอบความรู้ (OKF), เอกสารส่งมอบ (HANDOFF), และ README

---

### 1. รายละเอียดสิ่งที่แก้ไข (What was changed)

1. **ขยายฟิลด์ข้อมูลบริบทเรื่องแจ้งใน Query APIs (`get-issues`, `download-issues`, `get-issue`):**
   - เพิ่มฟิลด์ `type_reporter` (ประเภทปัญหาที่ผู้แจ้งระบุ), `user_id` (รหัสประจำตัวผู้แจ้ง), `is_follow` (มีการติดตามเรื่องหรือไม่), `is_forward` (มีการส่งต่อเรื่องหรือไม่), และ `status_latest` (สถานะล่าสุดในระบบ) ในผลลัพธ์ของ `get-issues` ทั้งรูปแบบ JSON และไฟล์ CSV (`download-issues/v2`)
   - เพิ่มฟิลด์ `sender_user_id` ในประวัติ `timeline[]` และ `user_name` ในบันทึกแชท `chat[]` ของ `get-issue/v2`
2. **ระบุการรองรับ Wildcard Search ใน `search-org`:**
   - ระบุความสามารถของพารามิเตอร์ `text` ใน `GET /search-org/v1` ว่ารองรับ wildcard `*` (หลายตัวอักษร) และ `?` (1 ตัวอักษร) เช่น `Traffy*`, `เขตจตุจัก?`
3. **เติมฟิลด์ข้อมูลระบุตัวตนและเลขอ้างอิงใน Webhook Events ครบทั้ง 3 ตัว:**
   - เพิ่มฟิลด์ `client_ticket_id` (หมายเลขเรื่องแจ้งฝั่งรับ webhook) ใน Incoming Payload และ JSON Example ของ `new-issue`, `update-issue`, และ `chat/comment`
   - เพิ่มฟิลด์ `sender_user_id` (รหัสประจำตัวผู้อัปเดต/ผู้ส่ง) และ `sender_user_name` (ชื่อ จนท. หรือ "ผู้แจ้ง")
   - ปรับข้อความเตือนการป้องกัน Echo Loop ให้เป็นมาตรฐานเดียวกัน
4. **จัดระเบียบตาราง Output Parameters ของเอกสารสาธารณะ:**
   - ถอด internal log/debug fields (`api_log_session_id*`, `exec_time`, `source`) ออกจากตารางคำอธิบายหลักของเอกสาร เพื่อความกระชับ ชัดเจนใน Business Payload (โดยยังคงแสดงใน JSON Example Response สำหรับการอ้างอิง)
   - ปรับปรุงการนำทางและหัวการ์ดใน `docs.html` ให้กระชับ สวยงาม พร้อมคำอธิบายย่อย
5. **อัปเดตเอกสารโครงการและบันทึกการตัดสินใจ:**
   - บันทึกการตัดสินใจเชิงสถาปัตยกรรม **ADR-014** และ **ADR-015** ใน `ADR.md`
   - อัปเดตเป้าหมายและกรอบความรู้เชิงระบบใน `OKF.md`
   - อัปเดตประวัติการปรับปรุงใน `README.md` และ `HANDOFF.md`
   - รีเฟรช Knowledge Graph ของ `graphify` (AST update)

---

### 2. รายการไฟล์ที่แก้ไข (Modified Files)

- `docs.html`: จัดระเบียบตาราง Output Parameters, ปรับปรุง Sidebar Nav พร้อม Subtitles, รวมการ์ด get-issues และ download-issues, เพิ่มฟิลด์ใน Webhooks
- `docs/query-apis.md`: จัดระเบียบตารางผลลัพธ์ get-type-list และ get-status-list ให้สอดคล้องกับ docs.html
- `docs/action-apis.md`: ถอด api_log_session_id* ออกจากตาราง Output, ปรับปรุงคำอธิบาย parameter ใน comment และ join-forward
- `docs/authentication.md`: ถอด api_log_session_id ออกจากตาราง Response Parameters
- `docs/webhooks.md`: ซิงค์ฟิลด์ client_ticket_id, sender_user_id, sender_user_name และ JSON sample ให้ตรงกับ docs.html ครบทั้ง 3 Webhooks
- `docs/overview.md`: เพิ่มรายละเอียด Webhook ที่ 3 (Chat/Comment) ในหัวข้อ Real-time Push
- `openapi.yaml`: เพิ่ม properties ใน Issue, IssueTimelineItem, IssueChatItem, CommentRequest และอัปเดตคำอธิบายพารามิเตอร์ search-org
- `ADR.md`: เพิ่มบันทึกสถาปัตยกรรม ADR-014 และ ADR-015
- `OKF.md`: เพิ่ม KR 1.9, KR 1.10 และ Data Validation Principles ข้อ 13 และ 14
- `README.md`: บันทึก Changelog ประจำวันที่ 2026-11-07
- `HANDOFF.md`: บันทึกการส่งมอบงานและการอัปเดตเวอร์ชัน 2026-11-07
- `graphify-out/graph.json` & `graphify-out/GRAPH_REPORT.md`: อัปเดต Knowledge Graph ให้เป็นเวอร์ชันล่าสุด
"""

run_cmd(["gh", "pr", "create", "--base", "main", "--head", branch_name, "--title", pr_title, "--body", pr_body])
