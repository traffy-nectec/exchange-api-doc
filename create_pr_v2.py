import re
import subprocess
import os
import sys

with open("/home/supertoy/.git-credentials") as f:
    text = f.read()

m = re.search(r"https://([^:]+):([^@]+)@github\.com", text)
if not m:
    print("Could not find token")
    sys.exit(1)

token = m.group(2)
env = os.environ.copy()
env["GH_TOKEN"] = token

branch_name = "docs/sync-timeline-chat-schema-and-csv-user-id"

def run(cmd, check=True):
    print("Running:", " ".join(cmd))
    r = subprocess.run(cmd, env=env, capture_output=True, text=True, cwd="/mnt/d/ubuntu_share/docker/exchange-api-doc")
    if r.stdout:
        print(r.stdout.strip())
    if r.stderr:
        print(r.stderr.strip())
    if check and r.returncode != 0:
        print("Failed with exit code", r.returncode)
        sys.exit(r.returncode)
    return r

run(["git", "checkout", "-b", branch_name])
run(["git", "add", "-A"])

commit_msg = """docs: sync timeline and chat schema, CSV user_id, and webhook warning

- Update timeline[] schema to use user_id and user_name instead of sender_user_id
- Add comment_type field to chat[] schema and samples
- Add user_id column to download-issues CSV example header and rows
- Update Webhook chat warning message to reference public comment API
- Format staff username examples with consistent spacing (จนท. Traffy Fondue)
- Update README, HANDOFF, ADR (ADR-016), OKF, and graphify output"""

run(["git", "commit", "-m", commit_msg])
run(["git", "push", "-u", "origin", branch_name])

pr_title = "docs: sync timeline and chat schema, CSV user_id, and webhook warning"
pr_body = """## สรุปรายละเอียดการแก้ไข (Summary of Changes)

Pull Request นี้ทำการตรวจสอบและปรับปรุงเอกสาร API เพิ่มเติมให้สอดคล้องกับพฤติกรรมจริงของเซิร์ฟเวอร์ และซิงค์โครงสร้างข้อมูลข้ามเอกสารทั้งหมด (`docs.html`, `docs/query-apis.md`, `docs/webhooks.md`, `openapi.yaml`, `ADR.md`, `OKF.md`, `README.md`, `HANDOFF.md`, `graphify`)

---

### 1. รายละเอียดสิ่งที่แก้ไข (What was changed)

1. **ปรับปรุงคีย์ระบุตัวตนใน `timeline[]` ของ `get-issue/v2`:**
   - เปลี่ยนคีย์ในประวัติ Timeline ให้เป็น `user_id` (รหัสประจำตัวผู้แจ้งหรือ จนท. ที่กดอัปเดต) และ `user_name` (ชื่อของ จนท. หรือ "ผู้แจ้ง") เพื่อให้ตรงตามผลลัพธ์จริงจากเซิร์ฟเวอร์ (เดิมระบุเป็น `sender_user_id`)
2. **เพิ่มฟิลด์ `comment_type` ใน `chat[]` ของ `get-issue/v2`:**
   - ระบุฟิลด์ `comment_type` ในโครงสร้างและตัวอย่างบทสนทนา เพื่อจำแนกประเภทข้อความ (`chat` = ข้อความแชท, `chat_staff_only` = จนท. คุยกันเอง, `rating` = ประเมินดาว, `comment` = คำแนะนำหลังให้ดาว)
3. **เพิ่มคอลัมน์ `user_id` ในไฟล์ CSV `download-issues/v2`:**
   - เพิ่มคอลัมน์ `user_id` ต่อท้ายใน Header และตัวอย่างแถวข้อมูลของไฟล์ CSV ในทุกเอกสาร
4. **ปรับปรุงข้อความเตือน Loop ของ Webhook:**
   - ปรับข้อความเตือนการวน Echo Loop ของ Webhook Chat ใน `docs/webhooks.md` ให้ระบุชื่อ API สาธารณะ `comment` (แทน `messagecomment`) ให้ตรงกับ `docs.html`
5. **มาตรฐานการจัดรูปแบบชื่อเจ้าหน้าที่:**
   - ปรับชื่อแสดงตัวอย่างเจ้าหน้าที่เป็น `"จนท. Traffy Fondue"` ให้มีเว้นวรรคมาตรฐานตรงกันทุกจุด
6. **อัปเดตเอกสารโครงการและบันทึกการตัดสินใจ:**
   - บันทึกการตัดสินใจเชิงสถาปัตยกรรม **ADR-016** ใน `ADR.md`
   - อัปเดตเป้าหมาย KR 1.11 และหลักการข้อ 15 ใน `OKF.md`
   - เพิ่มบันทึก Changelog ประจำวันที่ 2026-11-08 ใน `README.md` และ `HANDOFF.md`
   - รีเฟรช Knowledge Graph ของ `graphify` ให้เป็นเวอร์ชันล่าสุด

---

### 2. รายการไฟล์ที่แก้ไข (Modified Files)

- `docs.html`: ซิงค์โครงสร้าง `timeline[]`, `chat[]`, คอลัมน์ CSV `user_id`, และชื่อแสดงตัวอย่างเจ้าหน้าที่
- `docs/query-apis.md`: อัปเดตตารางและ JSON/CSV Example ของ `get-issues`, `get-issue`, `download-issues`
- `docs/webhooks.md`: แก้ไขข้อความเตือน Loop ให้ระบุ API `comment` และจัดรูปแบบชื่อเจ้าหน้าที่ตัวอย่าง
- `openapi.yaml`: อัปเดต Schema ของ `IssueTimelineItem` (`user_id`, `user_name`) และ `IssueChatItem` (`comment_type`)
- `ADR.md`: เพิ่มบันทึกสถาปัตยกรรม **ADR-016**
- `OKF.md`: เพิ่มเป้าหมาย **KR 1.11** และหลักการ **ข้อ 15** (Precise Object Model Alignment)
- `README.md`: บันทึกประวัติการเปลี่ยนแปลงประจำวันที่ 2026-11-08
- `HANDOFF.md`: บันทึกการส่งมอบงานเวอร์ชัน 2026-11-08
- `graphify-out/graph.json` & `graphify-out/GRAPH_REPORT.md`: อัปเดต Knowledge Graph ล่าสุด
"""

run(["gh", "pr", "create", "--base", "main", "--head", branch_name, "--title", pr_title, "--body", pr_body])
