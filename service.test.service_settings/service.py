import xbmc
import xbmcaddon

addon1 = xbmcaddon.Addon()
addon2 = xbmcaddon.Addon()
addon3 = xbmcaddon.Addon()


def print_settings():
    current_addon = xbmcaddon.Addon()
    xbmc.log("Setting addon1 = {}".format(addon1.getSetting('Setting1')), xbmc.LOGWARNING)
    xbmc.log("Setting addon2 = {}".format(addon2.getSetting('Setting1')), xbmc.LOGWARNING)
    xbmc.log("Setting addon3 = {}".format(addon3.getSetting('Setting1')), xbmc.LOGWARNING)
    xbmc.log("Setting new addon = {}".format(current_addon.getSetting('Setting1')), xbmc.LOGWARNING)


def run():
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        print_settings()
        monitor.waitForAbort(10)


if __name__ == '__main__':
    run()

