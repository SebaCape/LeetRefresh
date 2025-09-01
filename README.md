# LeetRefresh – LeetCode CLI Browser App

LeetRefresh is a browser-based terminal-style interface for browsing and practicing LeetCode problems. It allows users to load their LeetCode problem data from the API and interactively fetch problems by type and difficulty, all within a retro CLI aesthetic.

---

## Features

- Terminal-style interface with green-on-black CLI look.
- Upload your LeetCode `problems.json` to start.
- Fetch problems based on:
  - **Mode**: `random` (unsolved) or `review` (solved)
  - **Difficulty**: `easy`, `medium`, `hard`
- Display clickable problem links directly in the terminal.
- Step-by-step instructions on uploading JSON from [LeetCode API](https://leetcode.com/api/problems/all/).
- Works entirely in the browser; no backend required for basic usage.

---

## Getting Started

### 1. Download LeetCode JSON

1. Go to [LeetCode Problems API](https://leetcode.com/api/problems/all/) (Make sure you are logged in to leetcode on your browser!).  
2. Copy all text from the page.  
3. Paste it into Notepad or other text editor of choice.  
4. Save as `problems.json`.

### 2. Open the App

- Open `https://leetrefresh.onrender.com` in your browser.  
- Click **Choose File** and select your saved `problems.json`.  
- The CLI will display a welcome message with your username.

### 3. Using the CLI

- **Commands**:
  - `random` – fetch a new unsolved problem
  - `review` – fetch a previously solved problem
  - `status` – see loaded JSON info
  - `help` – view available commands
- After selecting a command, you will be prompted for difficulty (optional).
- Problem title and a clickable link will be displayed in the terminal.

---

## Example

```text
> Welcome, SebaCape
> Type "random" for a new problem or "review" to review a solved problem.
> random
> Choose difficulty (easy/medium/hard) or press Enter to skip:
> easy
> Problem: Two Sum → https://leetcode.com/problems/two-sum/
```

Usable under MIT License
