---
title: windows
date: 2019-12-05 01:08:55
tags: windows 
cover: /img/windows.jpg
---

## win32api  
鼠标左键按下  
`win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)`  
鼠标左键放开  
`win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)`  
鼠标右键按下  
`win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)`  
鼠标右键放开    
`win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)`  
设置鼠标位置  
`win32api.SetCursorPos((x, y))`    
键盘输入事件  
`win32api.keybd_event(VK_CODE[word], 0, 0, 0)`   
`win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)`  

***