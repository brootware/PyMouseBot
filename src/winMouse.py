import win32api
import win32con


def winMoveClick(posx, posy):
    # cursor move
    win32api.SetCursorPos((posx, posy))
    # click even call. Optional
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, posx, posy, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, posx, posy, 0, 0)
    print(f"[ + ] Window Mouse moved to pos x={posx} and pos y={posy}")
