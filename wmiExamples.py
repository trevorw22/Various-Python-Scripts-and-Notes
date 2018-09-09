# WMI control examples with python

import wmi
import win32api
import win32con

c = wmi.WMI()

for process in c.Win32_Process():
	print(process.ProcessId, process.Name)


# Get the mac and ip information from adapters

for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
  print(interface.Description, interface.MACAddress)
  for ip_address in interface.IPAddress:
    print(ip_address)


# Run a process minimised (doesn't start minimised)

SW_SHOWMINIMIZED = 1

startup = c.Win32_ProcessStartup.new(ShowWindow=SW_SHOWMINIMIZED)
pid, result = c.Win32_Process.Create(
  CommandLine="notepad.exe",
  ProcessStartupInformation=startup
)
print(pid)


# find the current wallpaper (doesn't work)

full_username = win32api.GetUserNameEx(win32con.NameSamCompatible)
for desktop in c.Win32_Desktop(Name=full_username):
  print(\
    desktop.Wallpaper or "[No Wallpaper]", \
    desktop.WallpaperStretched, desktop.WallpaperTiled)
