import dbus
import dbus.service
import dbus.mainloop.glib
from ConfigParser import ConfigParser

import gobject


class Service(dbus.service.Object):
    def __init__(self, message):
        self._message = message
        config_file = ConfigParser()
        config_file.read('./auth.config')
        self._access_key = config_file.get('auth', 'access_key')
        self._secret_key = config_file.get('auth', 'secret_key')
        print 'access_key: ', self._access_key, ' secret_key: ', self._secret_key

    def run(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus_name = dbus.service.BusName("com.makerfactory.photouploader.service", dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, "/com/makerfactory/photouploader")

        self._loop = gobject.MainLoop()
        print "Photo upload service running..."
        self._loop.run()
        print "Service stopped."

    @dbus.service.method("com.makerfactory.photouploader.service.Method")
    def upload_photo(self, path):
        print "upload photo method."
        print path


if __name__ == "__main__":
    Service("This is the service").run()