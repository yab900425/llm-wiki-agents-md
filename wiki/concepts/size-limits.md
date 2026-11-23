# 檔案太長會怎樣
- Codex：project_doc_max_bytes 預設 32 KiB，文件範例設為 65536；累積到上限就停止讀取，所以越具體（越靠近工作目錄）的檔案反而可能被截掉。[S5]
- Claude Code：建議每份 CLAUDE.md 少於 200 行，太長會佔 context 並降低遵守程度；匯入（@）不會省 context。[S4]
- Claude Code 的 auto memory：MEMORY.md 啟動時只讀前 200 行或 25KB。[S4]
- 因應：大型專案把規則拆到子目錄的檔案，而不是全塞在根目錄。[S5][S2]
相關：[[instruction-priority]]、[[writing-good-agents-md]]、[[../conflicts]] C3
