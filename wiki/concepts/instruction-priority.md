# 多份指示檔案誰優先
共通原則：越靠近目前工作位置的檔案越優先。但三份來源描述的機制不一樣，不要混在一起講。
- agents.md 官網：agent 讀「最近的那份」，離編輯檔案最近的優先；使用者在聊天中直接下的指令蓋過一切。[S2]
- Codex：從專案根往下走到目前目錄，每層最多採用一個檔案（override > AGENTS.md > fallback 名稱），全部串接，越近的排越後面所以蓋過前面；同層有 AGENTS.override.md 時取代 AGENTS.md。[S5]
- Claude Code：祖先目錄的 CLAUDE.md 全部串接而非覆蓋，順序由根到工作目錄，最近的最後讀；子目錄的檔案在讀寫該目錄的檔案時才載入。[S4]
- 驗證方式：Codex 可請它列出載入的指示來源，順序應為全域、專案根、子目錄。[S5] Claude Code 可用 /memory 看載入了哪些檔案。[S4]
- 沒有任何來源保證 agent 一定遵守；Claude 文件明說 CLAUDE.md 不保證一定遵守。[S4]
相關：[[agents-md]]、[[size-limits]]、[[../conflicts]] C5
