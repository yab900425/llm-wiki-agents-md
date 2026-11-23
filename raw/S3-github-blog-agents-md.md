# S3 擷取紀錄｜GitHub Blog：How to write a great agents.md
- 網址：https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- 讀取日期：2026-11-23
- 讀取方式：網頁擷取，讀到的是文章的**擷取摘要版**，不是逐字全文，措辭可能與原文略有差異。
- 作者／日期：Matt Nigh（頁面標示為 GitHub 專案經理總監）；2025-11-19 發布，2025-11-25 更新。

## 擷取重點（改寫）
- 作者分析「2,500+」份公開 repo 的 agent 檔案，主張失敗的和有效的差別很明顯：失敗的多半是空泛人設（例如「你是一個很有幫助的助理」）；有效的會定義專門角色、列出可執行指令、設明確邊界、給具體範例。
- 最好的檔案涵蓋六個面向：指令（commands）、測試、專案結構、程式風格、git 流程、邊界。
- 技巧：指令放前面並帶參數；用一小段真實程式碼示範風格，勝過長篇文字；明確寫「不要碰」的地方（機密、vendor 目錄、正式環境設定）；技術棧要寫版本；先從一個窄任務開始，出錯再補。
- 邊界分三層：Always do／Ask first／Never do。重要例子：測試用 agent 不可以刪掉失敗的測試。
- 文中提供多個範例 agent（docs、test、lint、api、dev-deploy）。

## 這篇文章的限制（擷取時發現）
- 沒有說明分析方法：沒有挑選條件、沒有定義什麼叫「有效」、沒有數字比例。唯一的頻率描述是「不要 commit 機密」是最常見的有用限制，也沒給數量。
- 標題或小節寫「六種 agent」，實際只描述五種。
- 同一個檔案有時寫 agents.md、有時寫 agent.md。
- dev-deploy 範例的指令是 npm run test，與「部署」的描述對不上。
- 檔案位置（.github/agents/）與 frontmatter 格式是 GitHub Copilot 自訂 agent 專用。
