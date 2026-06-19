# DigiClock
Inspired by BroCode's Digital Clock idea, this is my idea of a windows widget which shows time and changes colour based on accent colour chosen by your PC. Also has a transparent background. Not tested enough to check compatibility or OS stuff. Also has a scaling issue needed to be resolved. 

Anyways, to install is simple. Just download zip file and extract to a folder. Keep font and exe file in same folder or the font won't work.
I'll also give the code out soon in this repo. Just need to make a few aesthetic adjustments.

Here's the AI readme which looks cool because I haven't had much readme making experience yet.

# DigiClock 🕒

A sleek, minimalistic, and adaptive digital clock widget for Windows. Inspired by the simplicity of classic digital clocks, **DigiClock** dynamically syncs its accent color with your Windows system settings, ensuring it always feels like a native part of your desktop experience.

---

## ✨ Features

* **System-Synced Accents:** Automatically detects your Windows accent color and applies it to the clock interface.
* **True Transparency:** A fully frameless, transparent widget that stays on top of your windows.
* **Neon Glow:** Features a vibrant, high-saturation neon glow effect for excellent visibility.
* **Dynamic Scaling:** Resizes smoothly to fit any screen or window layout.
* **Drag-to-Move:** Simply click and drag anywhere on the clock to position it exactly where you want.
* **Native Context Menu:** Right-click the clock to quickly **Minimize** or **Close** the application.

---

## 🚀 Getting Started

### Installation
1. **Download:** Grab the latest release from the [Releases page](#).
2. **Extract:** Unzip the contents into a dedicated folder (e.g., `C:\Widgets\DigiClock`).
3. **Run:** Launch `DigiClock.exe`. 
   > **Note:** Ensure `DS-DIGIT.TTF` remains in the same folder as the `.exe` file to maintain the digital font style.

### Making it Auto-Start
Want the clock to greet you every time you sign in?
1. Right-click `DigiClock.exe` and select **Create shortcut**.
2. Press `Win + R` on your keyboard, type `shell:startup`, and press **Enter**.
3. Drag your new shortcut into the folder that opens.

---

## 🛠 Technical Details

Built with **Python** and **PyQt6**, this project leverages Windows registry hooks to pull system-level themes in real-time.

### Development Stack:
* **Language**: Python 3.14
* **GUI Framework**: PyQt6
* **System Hooks**: `winreg` (Windows Registry API)

---

## 💡 Customization & Contribution
Feel free to fork this repository, submit issues, or create pull requests. Whether you want to add new themes, support for multiple time zones, or custom alarms, contributions are highly encouraged!

---

## 📝 License
This project is open-source and available under the **MIT License**.

---
*Built with ❤️ for those who appreciate a clean desktop aesthetic.*
