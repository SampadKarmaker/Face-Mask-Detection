import pywintypes
import win32file
import win32con
from datetime import datetime

# Path to your file — update this to your actual file location
file_path = r"C:\Users\Sampad\Desktop\Face_Mask\plot.png"

# Desired new date/time: 17 June 2025, 10:30 AM
new_datetime = datetime(2025, 6, 25, 21, 30, 0)
win_time = pywintypes.Time(new_datetime)

# Open file handle with permission to update timestamps
handle = win32file.CreateFile(
    file_path,
    win32con.GENERIC_WRITE,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_ATTRIBUTE_NORMAL,
    None
)

# Set creation, accessed, and modified time to new time
win32file.SetFileTime(handle, win_time, win_time, win_time)
handle.close()

print("✅ File timestamps successfully updated to 17 June 2025, 10:30 AM!")
