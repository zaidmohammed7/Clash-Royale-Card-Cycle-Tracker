# Clash Royale Card Cycle Tracker

If you are just here to view the project and don't want to go through the entire project description check out this video!  
[Usage Demo](https://www.youtube.com/watch?v=gzkv1_iW1SI)

**Clash Royale Card Cycle Tracker Tracker** is a personal Python-based tool I developed to enhance my Clash Royale gaming experience. This project focuses on real-time tracking of an opponent's card cycle, elixir levels, and champion status by capturing specific regions of the screen. Leveraging libraries like OpenCV, PyAutoGUI, and PIL, this tool served as a practical application of image processing and automation techniques.

> **Note:** This project was created for personal use and is tailored specifically to my device's screen resolution and game layout. Due to hard-coded pixel coordinates and subsequent game updates, it may not function correctly on other devices or with the latest versions of Clash Royale.
## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Configuration](#configuration)
- [Limitations](#limitations)

## Features

- **Real-Time Card Tracking**: Monitors and displays the opponent's current hand and upcoming cards.
- **Elixir Monitoring**: Detects and updates the opponent's elixir level in real-time.
- **Champion Detection**: Identifies when champions like Skeleton King, Archer Queen, or Golden Knight are in play.
- **Custom GUI**: Utilizes a custom background image with clearly labeled sections for enhanced visibility.
- **Keyboard Integration**: Supports keyboard shortcuts for managing champion statuses.

## Prerequisites

Before running the Clash Royale Opponent Tracker, ensure you have the following:

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.6 or higher
- **Clash Royale**: Installed and running on your system
- **Required Assets**:
  - **Background Image**: `Background.png`
  - **Unknown Card Images**: Stored in the `Unknown/` directory (e.g., `unknown 1.png`, `unknown 2.png`, etc.)
  - **Elixir Bar Images**: Stored in the `Card elixir/` directory (e.g., `0.png`, `1.png`, ..., `10.png`)
  - **Champion Images**: `Skeleton King.png`, `Golden Knight.png`, `Archer Queen.png`


## Directory Structure

```plaintext
   Clash Royale Card Cycle Tracker/
   ├── Unknown/
   │   ├── unknown 1.png
   │   ├── unknown 2.png
   │   └── ... 
   ├── Card elixir/
   │   ├── 0.png
   │   ├── 1.png
   │   └── ...
   ├── card 1.png
   ├── card 2.png
   ├── ...
   ├── Skeleton King.png
   ├── Golden Knight.png
   ├── Archer Queen.png
   ├── Background.png
   ├── supercell-magic-webfont.ttf
   ├── Card Tacker.py
   └── Usage Demo.mp4
```

## Usage

1. **Positioning**
   
   - Ensure that Clash Royale is running and positioned correctly on your screen.
   - The tracker captures specific screen regions to monitor game elements. Adjust the screen resolution or positioning if necessary.

2. **Interpreting the GUI**
   
   - **Opponent's Cycle**: Displays the opponent's current hand and upcoming cards.
   - **Champion in Play**: Shows if a champion is currently active against you.
   - **Elixir Bar**: Continuously updates the opponent's elixir level.

3. **Keyboard Shortcuts**
   
   - **Spacebar**: Resets the champion kill status if a champion has been defeated.
  
4. **Run the Tracker**
   - Run the file "Card Tracker.py"

## Configuration

- **Screen Regions**

  The script captures specific regions of your screen to detect cards, elixir, and champions. If your game window is positioned differently or your screen resolution changes, you may need to adjust the coordinates in the script.

  ```python
  # Example Region: pag.screenshot('card 1.png', region=(752, 96, 60, 77))
  ```

## Limitations
- Device Specific: All pixel coordinates are hard-coded based on my device's screen resolution and game layout. The tool is not optimized for use on other devices.
- Not Maintained: Since its creation last year, Clash Royale has introduced more champions and new mechanics like evolutions, which are not accounted for in this tracker.
- Compatibility: Due to game updates, some features may not function as intended or may require manual adjustments to the script.
