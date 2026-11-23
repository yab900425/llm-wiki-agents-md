# CLAUDE.md 與 AGENTS.md 的關係
- CLAUDE.md 是 Claude Code 每次開新對話都會讀的持續性指示。[S4]
- 它是「引導」不是強制；要硬性禁止應該用 hook 或 permissions.deny。[S4]
- 四種範圍（廣到窄）：組織管理、使用者 ~/.claude/CLAUDE.md、專案 ./CLAUDE.md、本機 ./CLAUDE.local.md。[S4]
- Claude Code 可以讀 AGENTS.md（需 v2.1.277 以上）；預設只在找不到 CLAUDE.md 系列檔案時才讀。[S4]
- 兩邊都要支援時，建議 CLAUDE.md 只寫一行 `@AGENTS.md`，再在下面補 Claude 專屬內容。[S4]
- 也可用 symlink，但 Windows 上可能變成純文字，所以匯入（@）比較穩。[S4]
- agents.md 官網的支援工具清單沒有 Claude Code，頁面也沒提到 CLAUDE.md。[S2] 兩者並不矛盾，見 [[../conflicts]] C1、C2。
相關：[[agents-md]]、[[instruction-priority]]
