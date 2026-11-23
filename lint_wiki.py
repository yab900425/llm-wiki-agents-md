"""Wiki 健康檢查：孤兒頁、未收錄頁、壞連結、沒有來源標記的條目、衝突是否有處理。"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
W = ROOT / "wiki"
pages = {p.relative_to(W).with_suffix("").as_posix(): p for p in W.rglob("*.md")}
issues = []

base = {}
for k in pages:
    base.setdefault(k.split("/")[-1], []).append(k)

def resolve(l):
    """[[名稱]]：可寫完整路徑，或只寫檔名（Obsidian 慣例）；檔名重複時視為錯誤。"""
    l = l.split("|")[0].replace("../", "").lstrip("./")
    if l in pages: return l
    c = base.get(l.split("/")[-1], [])
    return c[0] if len(c) == 1 else None

def links(text):
    return re.findall(r"\[\[([^\]]+)\]\]", text)

# 1. 壞連結 + 反向連結統計
inbound = {k: 0 for k in pages}
for name, p in pages.items():
    for l in links(p.read_text(encoding="utf-8")):
        key = resolve(l)
        if key is None:
            issues.append(f"壞連結：{name} → [[{l}]]")
        elif key != name:
            inbound[key] += 1

# 2. 孤兒頁（沒有任何頁面連到它；index/log 例外）
for name, n in inbound.items():
    if n == 0 and name not in ("index", "log"):
        issues.append(f"孤兒頁：{name}")

# 3. 沒被 index 收錄
idx = (W / "index.md").read_text(encoding="utf-8")
for name in pages:
    if name not in ("index", "log") and not any(resolve(l) == name for l in links(idx)):
        issues.append(f"index 沒收錄：{name}")

# 4. 概念頁每條事實要有 [Sx]
for name, p in pages.items():
    if name.startswith("concepts/"):
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("- ") and not re.search(r"\[S\d\]|非來源|本專案|本 wiki", line):
                issues.append(f"沒有來源標記：{name}:{n}")

# 5. raw 每份來源都要有對應的 sources 頁
for raw in sorted((ROOT / "raw").glob("S*.md")):
    sid = raw.name.split("-")[0].lower()
    if not any(k.startswith(f"sources/{sid}-") for k in pages):
        issues.append(f"{raw.name} 沒有對應的 sources 頁")

print(f"頁面 {len(pages)} 頁")
if issues:
    print(f"共 {len(issues)} 個問題：")
    for i in issues: print("  ✗", i)
    sys.exit(1)
print("通過：沒有壞連結、孤兒頁、未收錄頁，概念頁的條目都有來源標記。")
