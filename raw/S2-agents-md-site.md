# S2 擷取紀錄｜agents.md 官方網站
- 網址：https://agents.md/
- 讀取日期：2026-11-23
- 讀取方式：網頁擷取，整頁讀完（約 11,000 字元）。
- 性質：格式的官方入口頁，無作者署名；頁尾標示 "AGENTS.md a Series of LF Projects, LLC"。

## 擷取重點（改寫）
- 定位：給 coding agent 看的簡單開放格式，等於「給 agent 的 README」。頁面寫「超過 60k 個開源專案」在用（連到 GitHub 程式碼搜尋，我沒有重跑該搜尋）。
- 分工：README 給人看；AGENTS.md 放 agent 需要、但會讓 README 變雜的細節（建置、測試、慣例）。
- 建議放的內容：專案概述、建置與測試指令、程式風格、測試說明、安全注意事項；也可放 commit/PR 規範、部署步驟等「會告訴新同事的事」。
- 使用步驟：放在 repo 根目錄；大型 monorepo 在各子專案再放一份。
- 優先順序：agent 讀「最近的」那份，離編輯檔案最近的優先；使用者在聊天中直接下的指令蓋過一切。
- 欄位：沒有必填欄位，就是一般 Markdown，標題可自訂。
- 提到 OpenAI 主 repo 有 88 份 AGENTS.md（頁面寫 "at time of writing"，沒給日期）。
- 來源與管理：由 OpenAI Codex、Amp、Google Jules、Cursor、Factory 等協作出現；現由 Agentic AI Foundation（Linux Foundation 旗下）管理。
- 支援工具清單（logo 牆）：Codex、Jules、Factory、Aider、goose、opencode、Zed、Warp、VS Code、Devin、Junie、Amp、Cursor、RooCode、Gemini CLI、Kilo Code、Windsurf、Augment Code、GitHub Copilot coding agent 等。**清單上沒有 Claude Code，頁面也完全沒提到 CLAUDE.md。**
- 常見問答：舊檔可改名成 AGENTS.md 再建 symlink 保持相容；Aider 要在 .aider.conf.yml 設 read；Gemini CLI 要在設定檔指定檔名；agent 會執行檔案裡列出的測試指令；文件應視為持續更新的活文件。
