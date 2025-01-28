
```markdown
# Stremio Cache Cleaner

This Python script helps you clean the cache of your Stremio server to free up disk space, and shows a notification with the results.

## Requirements

- Python 3
- `libnotify` (for notifications)
- `notify-send` (for sending notifications)
- `dunst` (for customizable notifications)


2. **Install Dependencies**: Install Python dependencies (if any are listed in `requirements.txt`).

   ```bash
   pip install -r requirements.txt
   ```

   Or install `libnotify` and `dunst` for notifications:

   ```bash
   sudo pacman -S libnotify dunst
   ```

3. **Install dunst (if not already installed)**:
   If you don't have `dunst` installed, run:

   ```bash
   sudo pacman -S dunst
   ```

## Usage

1. **Run the Script**: Execute the script to clean your Stremio cache:

   ```bash
   python3 clean_stremio_cache.py
   ```

   This will:
   - Check the cache directory.
   - Clean the cache (freeing up disk space).
   - Show a notification after completion with the result (how much space was freed).

2. **Notification**: After the cache is cleaned, a notification will pop up showing the result of the operation. If you have `dunst` installed, it will display a styled notification.

---

## Customizing dunst Notifications

You can customize the appearance of your notifications (such as background color, font, and corner radius) by editing the `dunst` configuration file. Here’s how you can do it:

### Location of the dunst Configuration File

The `dunst` configuration file is typically located in:

```bash
~/.config/dunst/dunstrc
```

### Customizing Your Notifications

1. **Change the Background Color**: To change the background color of your notifications, find the `background` field in the `urgency_*` sections (low, normal, critical) and adjust the hex color value.

   Example:
   ```ini
   [urgency_normal]
   background = "#232323"  # Change this to your preferred color
   foreground = "#f0f0f0"
   ```

2. **Set Corner Radius for Rounded Corners**: To give your notifications rounded corners, set the `corner_radius` value to a positive integer (e.g., `corner_radius = 10`).

   Example:
   ```ini
   [global]
   corner_radius = 10  # Adjust for rounded corners
   ```

3. **Change Font**: Change the font for your notifications by adjusting the `font` setting.

   Example:
   ```ini
   [global]
   font = Noto Sans 12
   ```

4. **Position of Notifications**: You can also adjust the position of the notifications on the screen using the `geometry` option.

   Example:
   ```ini
   [global]
   geometry = "320x5+10+60"  # Set the position and size of the notification
   ```

### Restart dunst for Changes to Take Effect

Once you've edited the configuration file, restart `dunst` to apply the changes:

1. **Restart dunst**:
   ```bash
   pkill dunst
   dunst &
   ```

### Example Customization

Here’s an example of a simple customization in the `dunstrc`:

```ini
[global]
geometry = "320x5-25+60"
corner_radius = 10
frame_color = "#232323"
background = "#222222"
foreground = "#ffffff"
font = "Noto Sans 12"
```

This configuration gives your notifications rounded corners, a dark background with light text, and uses a specific font.

---

## Why Dunst?

I initially tried using the default `xfce4-notifyd` for notifications, but I wasn't able to make it work properly on my setup. As a result, I considered `dunst` as an alternative. Dunst is a highly customizable notification daemon that allows much more control over the appearance and behavior of notifications, making it a better fit for this project.




### Steps to Compile the Python App Using PyInstaller

1. **Install PyInstaller**:
   First, make sure PyInstaller is installed in your virtual environment or globally.

   ```bash
   pip install pyinstaller
   ```

2. **Compile the Script**:
   Once PyInstaller is installed, navigate to the folder where your Python script (`clean_stremio_cache.py`) is located, and run the following command:

   ```bash
   pyinstaller --onefile clean_stremio_cache.py
   ```

   - `--onefile`: This flag tells PyInstaller to bundle everything into a single executable file.
   - `clean_stremio_cache.py`: This is the Python script you want to compile.

   If your script relies on external packages or resources (like images or configuration files), PyInstaller will attempt to bundle them as well.

3. **Find the Executable**:
   After running the above command, PyInstaller will generate several directories and files. The compiled executable will be inside the `dist` folder.

   ```bash
   ls dist/
   ```

   You'll see an executable file named `clean_stremio_cache` (or `clean_stremio_cache.exe` on Windows).

4. **Test the Executable**:
   You can now run the compiled binary directly from the terminal:

   ```bash
   ./dist/clean_stremio_cache
   ```

   This will execute the application just like running the Python script.

5. **Distribute the Executable**:
   You can now distribute the executable to others, and they don't need Python installed to run the app.

### Additional Tips:
- **Customizing the Icon**: If you want to set a custom icon for your application (for example, to make it look like a native app), you can use the `--icon` option in PyInstaller.
  Example:
  ```bash
  pyinstaller --onefile --icon=app_icon.ico clean_stremio_cache.py
  ```
- **Debugging**: If there are any issues during the compilation process, you can use the `--debug` option to get more information.
  
  ```bash
  pyinstaller --onefile --debug clean_stremio_cache.py
  ```

- **Optional Arguments**:
  - `--add-data="path/to/data:."`: This is used if your app has additional data files (e.g., configuration files). You'd replace `"path/to/data"` with the path to your file or directory.




## Installation on Arch Linux

### 1. Install dependencies
Before building the package, make sure you have the required dependencies installed:

```bash
sudo pacman -S python python-pip python-virtualenv dunst libnotify
```

### 2. Build and install the package
Clone the repository and navigate to the project directory, then run the following command to build and install the application:

```bash
makepkg -si
```

This will:
- Build the package
- Install it on your system

### 3. Running the application
After installation, you can run the application using the following command:

```bash
clean_stremio_cache
```

It will clean the Stremio cache and display a notification when done.

## Customizing Notifications (with Dunst)
The notification style can be customized by editing the **dunstrc** file, located at `~/.config/dunst/dunstrc`.

You can change the colors, icons, and other properties to match your preferences.

For example, to change the background color or add rounded corners, you can edit the following settings in `dunstrc`:

```ini
[global]
    geometry = "320x5-25+60"
    corner_radius = 10
    frame_width = 1
    frame_color = "#232323"

[urgency_low]
    background = "#232323"
    foreground = "#a8a8a8"

[urgency_normal]
    background = "#232323"
    foreground = "#a8a8a8"

[urgency_critical]
    background = "#d64e4e"
    foreground = "#f0e0e0"
    frame_color = "#d64e4e"
```

Make sure to restart Dunst after making changes to see them take effect:

```bash
pkill dunst && dunst &
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

