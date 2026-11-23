# AGENTS.md｜AGENTS.md 主題 LLM Wiki

這個資料夾是一個 LLM Wiki，主題是「AGENTS.md（寫給 AI 看的專案說明書）」。
AI 在這裡的工作是維護 wiki、並用 wiki 產生教學簡報。請先讀完這份文件再動手。

## 1. 三層結構（照 Karpathy 的 LLM Wiki 做法）
- `raw/`：原始來源的擷取紀錄（網址、讀取日期、讀取範圍、重點）。**只新增，不修改**。
- `wiki/`：整理後的知識頁（繁體中文）。AI 負責維護，可改可增。
  - `wiki/index.md`：所有頁面的目錄，每次 ingest 都要更新。
  - `wiki/log.md`：只往後加的紀錄，格式 `## [日期] 動作 | 標題`。
  - `wiki/sources/`：每個來源一頁摘要。
  - `wiki/concepts/`：概念頁。
  - `wiki/conflicts.md`：來源之間說法不一致的地方與處理結果。
- `slides/`：由 wiki 產生的 HTML 簡報（`slides.json` → `build_slides.py` → `index.html`）。

## 2. 核心規則
1. 不憑記憶寫內容。每個事實都要能追到 `wiki/sources/` 的某一頁。
2. 只用「完整讀過」的來源當依據。搜尋結果的摘要只能拿來找網址，不能直接當事實寫進 wiki。
3. 來源之間說法不同，不選邊猜，記進 `wiki/conflicts.md`，並說明最後採用哪一個、為什麼（官方文件優先於第三方文章）。
4. 來源沒說的就寫「來源未提」，不補。
5. 用自己的話整理，不貼原文長段落；引用最多一小句並標來源。
6. 來源本身有缺點（沒有研究方法、前後矛盾）要寫在該來源頁的「限制」。

## 3. Ingest 流程（每個來源都照做）
1. 完整讀取來源，把網址、讀取日期、讀取範圍寫進 `raw/Sx-*.md`。
2. 在 `wiki/sources/sx-*.md` 寫摘要：重點、數字、限制。
3. 更新或新增 `wiki/concepts/` 受影響的頁面，每條事實後面標來源 `[S1]`～`[S5]`。
4. 與既有頁面比對，有衝突就寫進 `wiki/conflicts.md`。
5. 更新 `wiki/index.md`，並在 `wiki/log.md` 加一筆。

## 4. 做簡報的流程
1. 先查 `wiki/index.md`，再讀需要的概念頁。
2. 在 `slides/slides.json` 寫每一頁。每個事實都要列出 `refs`（用到的 wiki 頁）與 `must_contain`（這個事實裡的關鍵數字或名詞）。
3. 執行 `python3 slides/check_slides.py`：檢查引用的頁面存在、關鍵數字真的出現在引用頁裡。沒過就改 slides.json 或回頭查 wiki，**不可為了過關而刪掉檢查**。
4. 通過後執行 `python3 slides/build_slides.py` 產生 `slides/index.html`。
5. 最後執行 `python3 lint_wiki.py`：找孤兒頁、沒被 index 收錄的頁、沒有來源標記的條目。

## 5. 不可以做的事
- 不可修改 `raw/` 已有的檔案。
- 不可把沒讀過的網頁寫成「來源」。
- 不可在簡報中放 wiki 裡沒有的數字或說法。
- 不可使用外部 CDN；簡報是單一 HTML，直接開檔或放 GitHub Pages 即可。
