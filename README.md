
```markdown
# Stremio Cache Cleaner

This Python script helps you clean the cache of your Stremio server to free up disk space, and shows a notification with the results.

---

## Requirements

- Python 3
- `libnotify` (for notifications)
- `notify-send` (for sending notifications)
- `dunst` (for customizable notifications)

---

## Installation

### Clone the Repository
Download or clone this repository to your local machine:

```bash
git clone https://github.com/jekomaster/stremio_clean_cache-.git
cd stremio_clean_cache-
```

### Install Dependencies
Install Python dependencies (if any are listed in `requirements.txt`):

```bash
pip install -r requirements.txt
```

Or install `libnotify` and `dunst` for notifications:

```bash
sudo pacman -S libnotify dunst
```

---

## Usage

1. **Run the Script**: Execute the script to clean your Stremio cache:

   ```bash
   python3 clean_stremio_cache.py
   ```

2. **Compiled Binary (Optional)**: If you prefer to use the compiled binary:

   ```bash
   ./clean_stremio_cache
   ```

   This requires the binary to be built using `makepkg` (see below).

3. **Notifications**: After cleaning the cache, a notification will display the result.

---

## Building from Source (Arch Linux)

1. **Build the Package**:
   ```bash
   makepkg -si
   ```

2. **Run the Compiled Binary**:
   ```bash
   ./clean_stremio_cache
   ```

---

## Customizing Notifications with dunst

You can customize the appearance of notifications by editing the `dunst` configuration file.

### Edit Configuration
The `dunst` configuration file is typically located in:

```bash
~/.config/dunst/dunstrc
```

#### Key Settings to Modify:
- **Background Color**:
  ```ini
  [urgency_normal]
  background = "#222222"  # Replace with your preferred color
  ```
- **Corner Radius for Rounded Corners**:
  ```ini
  [global]
  corner_radius = 10
  ```
- **Font**:
  ```ini
  [global]
  font = "Noto Sans 12"
  ```
- **Notification Position**:
  ```ini
  [global]
  geometry = "320x5-25+60"
  ```

#### Restart dunst:
After making changes, restart `dunst` to apply them:

```bash
pkill dunst
dunst &
```

---

## Why Dunst?

I initially tried using the default `xfce4-notifyd` for notifications, but I wasn't able to make it work properly on my setup. As a result, I considered `dunst` as an alternative. Dunst is a highly customizable notification daemon that allows much more control over the appearance and behavior of notifications, making it a better fit for this project.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

This version incorporates the necessary adjustments while keeping the structure clean and user-friendly! Let me know if you need help uploading it to your repository or refining further.