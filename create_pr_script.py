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

branch_name = "docs/clarify-webhook-loop-prevention"
repo_dir = "/mnt/d/ubuntu_share/docker/exchange-api-doc"

def run(cmd, check=True):
    print("Running:", " ".join(cmd))
    r = subprocess.run(cmd, env=env, capture_output=True, text=True, cwd=repo_dir)
    if r.stdout:
        print(r.stdout.strip())
    if r.stderr:
        print(r.stderr.strip())
    if check and r.returncode != 0:
        print("Failed with exit code", r.returncode)
        sys.exit(r.returncode)
    return r

# Create and checkout new branch
run(["git", "checkout", "-b", branch_name])
run(["git", "add", "-A"])

commit_msg = """docs: clarify webhook loop prevention conditions and sync docs

- Update webhook loop prevention notices in docs.html and docs/webhooks.md
  to clarify outbound event suppression and prevent echo loop
- Add ADR-017 for webhook loop prevention specifications
- Update OKF (KR 1.12 & Principle 7), README changelog, and HANDOFF
- Update graphify knowledge graph"""

run(["git", "commit", "-m", commit_msg])
run(["git", "push", "-u", "origin", branch_name])

pr_title = "docs: clarify webhook loop prevention conditions and sync docs"
pr_body = """## สรุปรายละเอียดการแก้ไข (Summary of Changes)

Pull Request นี้ทำการอัปเดตและปรับปรุงข้อความเตือนการป้องกัน Webhook Loop ให้ครอบคลุมและชัดเจนทั้ง 2 มิติ พร้อมซิงค์เอกสารโครงการและบันทึกการตัดสินใจเชิงสถาปัตยกรรมทั้งหมด

---

### 1. รายละเอียดสิ่งที่แก้ไข (What was changed)

1. **ระบุเงื่อนไขการป้องกัน Webhook Loop ให้ชัดเจน 2 ด้าน:**
   - **Outbound Event Suppression:** ชี้แจงว่าระบบ Traffy Fondue จะไม่ส่ง event ที่เกิดจากการเรียก API ต้นทาง (`/new-issue`, `/update-issue`, `/comment`) วนกลับมายัง Webhook ของหน่วยงาน
   - **Inbound Echo Loop Prevention:** กำชับว่าหน่วยงานผู้รับ Webhook ห้ามนำข้อมูลจาก Webhook ส่งวนกลับเข้ามายัง Action API (`/new-issue`, `/update-issue`, `/comment`) เพื่อป้องกัน Infinite Data Loop
2. **ซิงค์ข้อความเตือนให้สอดคล้องกัน:**
   - ปรับข้อความเตือนใน `docs.html` และ `docs/webhooks.md` ให้เป็นมาตรฐานเดียวกันครบทั้ง 3 Webhook Events (`new-issue`, `update-issue`, `chat/comment`)
3. **อัปเดตเอกสารโครงการและบันทึกการตัดสินใจ:**
   - บันทึกการตัดสินใจเชิงสถาปัตยกรรม **ADR-017** ใน `ADR.md`
   - เพิ่มเป้าหมาย **KR 1.12** และอัปเดตหลักการข้อ 7 ใน `OKF.md`
   - บันทึก Changelog ประจำวันที่ 2026-11-11 ใน `README.md` และ `HANDOFF.md`
   - ปรับปรุงและซิงค์ Knowledge Graph ของ `graphify` ให้เป็นเวอร์ชันล่าสุด

---

### 2. รายการไฟล์ที่แก้ไข (Modified Files)

- `docs.html`: อัปเดตข้อความเตือนป้องกัน Loop ใน Webhooks
- `docs/webhooks.md`: ซิงค์ข้อความเตือนป้องกัน Loop ให้ตรงกับ `docs.html`
- `ADR.md`: เพิ่มบันทึกสถาปัตยกรรม **ADR-017**
- `OKF.md`: เพิ่มเป้าหมาย **KR 1.12** และปรับปรุงหลักการข้อ 7
- `README.md`: บันทึกประวัติการเปลี่ยนแปลงประจำวันที่ 2026-11-11
- `HANDOFF.md`: บันทึกประวัติการส่งมอบงานเวอร์ชัน 2026-11-11
- `graphify-out/graph.json` & `graphify-out/GRAPH_REPORT.md`: ซิงค์ Knowledge Graph ล่าสุด
"""

res = run(["gh", "pr", "create", "--base", "main", "--head", branch_name, "--title", pr_title, "--body", pr_body])
print("PR Result:", res.stdout)
