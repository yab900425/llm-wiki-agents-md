# S1 擷取紀錄｜Karpathy「LLM Wiki」idea file
- 網址：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 讀取日期：2026-11-23
- 讀取方式：網頁擷取，gist 本文完整讀到；底下留言串只拿到摘要，**不當依據**。
- 作者／日期：karpathy；頁面顯示 Created 2026-04-04，1 次修訂。
- 性質：作者自稱 "idea file"，刻意寫得抽象，具體做法交給使用者與 LLM 決定。

## 擷取重點（改寫，非原文）
- 一般 RAG（例：NotebookLM、檔案上傳）每次提問都重新檢索片段再回答，知識不會累積。
- 提出的做法：LLM 在「使用者」和「原始資料」之間，持續維護一組互相連結的 markdown 頁面。新資料進來時，LLM 讀完、抽重點、更新既有頁面、標出和舊說法的矛盾。
- 三層：raw sources（不可改，真相來源）／wiki（LLM 全權維護）／schema（CLAUDE.md 或 AGENTS.md，規定結構與工作流程）。
- 三個操作：ingest（一次一份，作者偏好邊看邊討論，一份可能動到 10–15 頁）、query（讀 index 再深入；好答案要存回 wiki）、lint（找矛盾、過時說法、孤兒頁、缺頁、缺交叉連結）。
- index.md：內容導向的頁面目錄，每頁一行摘要。log.md：只往後加的時間紀錄，標題格式固定，方便用 grep 查。
- 規模：作者說只靠 index 在「約 100 份來源、數百頁」仍運作良好，不需要向量檢索。
- 提到的工具：Obsidian、Obsidian Web Clipper、Marp、Dataview、qmd、git（皆為選用）。
- 作者說明：目錄結構、頁面格式、工具都是選用且可調整。
