# S4 擷取紀錄｜Claude Code 官方文件：How Claude remembers your project
- 網址：https://code.claude.com/docs/en/memory
- 讀取日期：2026-11-23
- 讀取方式：網頁擷取，分兩次讀完全頁（約 55,000 字元），非摘要。
- 性質：Anthropic 官方文件。

## 擷取重點（改寫）
- CLAUDE.md 是每次開新對話都會讀的持續性指示；它是「引導」不是強制，要硬性禁止應用 hook 或 permissions.deny。
- 四種範圍（廣到窄）：組織管理、使用者（~/.claude/CLAUDE.md）、專案（./CLAUDE.md 或 ./.claude/CLAUDE.md）、本機（./CLAUDE.local.md，建議加進 .gitignore）。
- 載入：啟動時讀工作目錄與其上層所有目錄的 CLAUDE.md；全部串接不是覆蓋，順序由根目錄到工作目錄，最近的最後讀。子目錄的檔案在 Claude 第一次讀寫該目錄的檔案時才載入。
- 匯入：用 @路徑 把別的檔案展開進來，最多 4 層；匯入不會省 context。
- 與 AGENTS.md：Claude Code 可以讀 AGENTS.md（需 v2.1.277 以上）。預設只在工作目錄以上**找不到** CLAUDE.md 系列檔案時才讀 AGENTS.md。同時要給多種工具用時，建議 CLAUDE.md 內寫一行 `@AGENTS.md`，下面再補 Claude 專屬內容；也可用 symlink，但 Windows 上可能變成純文字，所以匯入較穩。
- 寫法建議：要具體可驗證（「用 2 個空格縮排」勝過「好好排版」）；每份建議少於 200 行；用標題與條列；移除互相矛盾的內容；/doctor prompt-audit 可檢查過時或衝突內容。
- /init 可產生起始 CLAUDE.md；/memory 可查看目前載入哪些檔案。
- 另有 auto memory（Claude 自己寫的筆記，存在 ~/.claude/projects/<專案>/memory/，MEMORY.md 是索引，啟動時讀前 200 行或 25KB）。
- 注意：CLAUDE.md 以使用者訊息形式送出，不保證一定遵守。
