# S5 擷取紀錄｜OpenAI Codex 指南：Custom instructions with AGENTS.md
- 網址：https://developers.openai.com/codex/guides/agents-md（讀取時轉址到 https://learn.chatgpt.com/docs/agent-configuration/agents-md）
- 讀取日期：2026-11-23
- 讀取方式：網頁擷取，整頁讀完（約 47,500 字元）。
- 性質：OpenAI 官方文件。

## 擷取重點（改寫）
- 每次執行時在啟動階段建立一次指示鏈，沒有快取；改了之後重開就會重建。
- 全域：Codex home（預設 ~/.codex）裡先找 AGENTS.override.md，沒有再找 AGENTS.md，只取第一個非空檔。
- 專案：從專案根目錄（通常是 Git 根）往下走到目前目錄，每一層依序找 AGENTS.override.md、AGENTS.md、再來是 project_doc_fallback_filenames 列的名稱，**每層最多採用一個檔案**。
- override：同一層有 AGENTS.override.md 時，它取代同層的 AGENTS.md。
- 合併：從根目錄往下串接，中間空一行；越靠近目前目錄的越後面，所以會蓋過前面的指引；空檔跳過。
- 大小限制：project_doc_max_bytes 預設 32 KiB，範例設成 65536；累積到上限就停止讀取，所以越靠近工作目錄（越具體）的檔案反而可能被截掉。
- 驗證：可以請 Codex「列出載入了哪些指示檔案」，應該依序是全域、專案根、子目錄。
- 建議：全域放通用工作約定；repo 根放整體規範；越專門的規則越靠近程式碼；保持精簡，太大就拆到子目錄。
