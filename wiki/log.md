# 操作紀錄（只往後加）
## [2026-11-23] setup | 決定主題與結構
主題：AGENTS.md。結構採 Karpathy 的 raw / wiki / schema 三層。先寫好 AGENTS.md（schema）再開始 ingest。
## [2026-11-23] search | 找來源
用搜尋找到 5 個候選網址（含 Claude Code 與 Codex 官方文件）。搜尋摘要發現「Claude Code 不讀 AGENTS.md」的說法，標記為待查（見 conflicts C1）。
## [2026-11-23] ingest | S1 Karpathy LLM Wiki
完整讀 gist 本文；留言串只有摘要，不採用。新增 concepts/llm-wiki-pattern、schema-file。
## [2026-11-23] ingest | S2 agents.md 官網
整頁讀完。新增 concepts/agents-md。發現官網清單沒列 Claude Code（C2）。
## [2026-11-23] ingest | S3 GitHub Blog
讀到的是擷取摘要版。新增 concepts/writing-good-agents-md、boundaries。發現文章前後不一致（C4）。
## [2026-11-23] ingest | S4 Claude Code 官方文件
整頁讀完。確認 Claude Code 可讀 AGENTS.md，推翻搜尋摘要的說法（C1）。新增 concepts/claude-md、size-limits、instruction-priority。
## [2026-11-23] ingest | S5 Codex 官方文件
整頁讀完。釐清 32 KiB 與 65536 的差別（C3）。補充 instruction-priority、size-limits。
## [2026-11-23] conflicts | 整理 C1–C5
三家「優先」的機制不同（C5），簡報不能用「覆蓋」一詞帶過。
