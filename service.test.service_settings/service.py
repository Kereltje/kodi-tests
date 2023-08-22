
import threading
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()

def print_settings(prefix='Thread -'):
    current_addon = xbmcaddon.Addon()
    xbmc.log("{} Setting 1 = {}".format(prefix, addon.getSetting('Setting1')), xbmc.LOGWARNING)
    xbmc.log("{} Setting 2 = {}".format(prefix, addon.getSetting('Setting2')), xbmc.LOGWARNING)
    xbmc.log("{} Setting 1 current addon = {}".format(prefix, current_addon.getSetting('Setting1')), xbmc.LOGWARNING)
    xbmc.log("{} Setting 2 current_addon = {}".format(prefix, current_addon.getSetting('Setting2')), xbmc.LOGWARNING)


def run():
    monitor = xbmc.Monitor()
    state = False
    while not monitor.abortRequested():
        print_settings()
        state = not state
        addon.setSetting('Setting2', str(state).lower())
        monitor.waitForAbort(10)


if __name__ == '__main__':
    # run()
    threading.Thread(target=run, daemon=True).start()
    monitor = xbmc.Monitor()
    monitor.waitForAbort(5)
    while not monitor.abortRequested():
        print_settings('Main -')
        monitor.waitForAbort(10)
