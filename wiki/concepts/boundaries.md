# 邊界：Always／Ask first／Never
- S3 建議把邊界分三層：Always do（一律做）、Ask first（先問）、Never do（不要做）。[S3]
- Always 的例子：寫入 src/ 和 tests/、commit 前先跑測試。[S3]
- Never 的例子：commit 機密、改 node_modules 或 vendor 目錄、改正式環境設定。[S3]
- Ask first 的例子：改資料庫結構、加新套件、改 CI/CD。[S3]
- 重要例子：測試用 agent 不可以刪掉失敗的測試。[S3]
- 要擋死的事不要只靠文字：Claude 文件說 CLAUDE.md 不保證遵守，硬性禁止要用 hook 或 permissions.deny。[S4]
相關：[[writing-good-agents-md]]、[[claude-md]]
