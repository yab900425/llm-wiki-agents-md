# AGENTS.md 主題 LLM Wiki ＋ 教學簡報

主題：AGENTS.md（寫給 AI 看的專案說明書）。先建 LLM Wiki（5 份來源），再用 Wiki 做一份教學型 HTML 簡報。

- 簡報（GitHub Pages）：https://yab900425.github.io/llm-wiki-agents-md/slides/
- Wiki 目錄：`wiki/index.md`；來源衝突紀錄：`wiki/conflicts.md`；操作紀錄：`wiki/log.md`
- 規則（schema）：`AGENTS.md`（`CLAUDE.md` 只有一行 `@AGENTS.md`）

## 結構
```
raw/        原始來源的擷取紀錄（只增不改）
wiki/       整理後的知識頁：sources/ 來源摘要、concepts/ 概念頁、index、log、conflicts
slides/     slides.json → build_slides.py → index.html；check_slides.py 檢查簡報能否對回 wiki
lint_wiki.py  Wiki 健康檢查
```

## 流程（graph）
```
找來源 → 完整讀取 → 來源驗證關卡 → ingest 進 wiki → 衝突比對 → lint
                                                                  ↓
   重新產生 ← 不通過 ← 簡報檢查（check_slides）← 查 wiki 寫 slides.json
                                  ↓ 通過
                        build_slides → 簡報 HTML
```

## 指令
```bash
python3 slides/check_slides.py   # 簡報檢查
python3 slides/build_slides.py   # 產生 slides/index.html
python3 lint_wiki.py             # wiki 健康檢查
```
