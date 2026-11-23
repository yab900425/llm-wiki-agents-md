"""簡報檢查：每頁的說法要能對回 wiki。沒過就改 slides.json 或回頭補 wiki，不要刪檢查。"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "slides" / "slides.json").read_text(encoding="utf-8"))
errors, warns = [], []
cache = {}

def page(ref):
    p = ROOT / ref
    if ref not in cache:
        cache[ref] = p.read_text(encoding="utf-8") if p.exists() else None
    return cache[ref]

def shown_text(s):
    parts = [s.get("title", ""), s.get("sub", ""), s.get("note", ""), s.get("code", "")]
    parts += s.get("items", [])
    parts += s.get("head", [])
    for r in s.get("rows", []):
        parts += r
    for c in s.get("cols", []):
        parts.append(c["head"]); parts += c["items"]
    return "\n".join(parts)

for i, s in enumerate(data["slides"], 1):
    tag = f"第 {i} 頁《{s.get('title','')[:14]}》"
    refs = s.get("refs", [])
    if not refs:
        errors.append(f"{tag}：沒有 refs")
    texts = []
    for r in refs:
        t = page(r)
        if t is None:
            errors.append(f"{tag}：引用的頁面不存在 {r}")
        else:
            texts.append(t)
    union = "\n".join(texts)
    if s["layout"] != "sources" and not s.get("facts"):
        errors.append(f"{tag}：沒有任何 facts")
    # 1. 每個 fact 的關鍵字要出現在它引用的頁面
    for f in s.get("facts", []):
        ftxt = "\n".join(page(r) or "" for r in f["refs"])
        for m in f["must"]:
            if m not in ftxt:
                errors.append(f"{tag}：「{f['claim']}」的關鍵字「{m}」不在 {f['refs']}")
        if not f["refs"]:
            errors.append(f"{tag}：fact 沒有 refs")
    # 2. 簡報上出現的數字，必須在引用頁面裡出現過
    shown = shown_text(s)
    for num in set(re.findall(r"\d[\d,.]*\d|\d", shown)):
        if num not in union:
            errors.append(f"{tag}：簡報上的數字「{num}」不在引用的 wiki 頁面裡")
    # 3. 引用的概念頁，至少要有來源標記
    for r in refs:
        t = page(r)
        if t and r.startswith("wiki/concepts/") and not re.search(r"\[S\d\]", t):
            warns.append(f"{tag}：{r} 沒有任何 [Sx] 來源標記")

for w in warns: print("警告：", w)
if errors:
    print(f"\n共 {len(errors)} 個問題：")
    for e in errors: print("  ✗", e)
    sys.exit(1)
print(f"通過：{len(data['slides'])} 頁，每頁都能對回 wiki，簡報上的數字都在引用頁面裡。")
