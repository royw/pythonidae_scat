# coding=utf-8
"""
The Pythonidae Scat application.

"""
from fullmonty.graceful_interrupt_handler import GracefulInterruptHandler
from fullmonty.simple_logger import Logger, FileLogger

__docformat__ = 'restructuredtext en'
__all__ = ("Pythonidae ScatApp",)


class PythonidaeScatApp(object):
    """
    This is the application class.

    Usage::

        cli = Pythonidae ScatCLI()
        cli.execute(Pythonidae ScatApp())

    """

    def __init__(self):
        """
        The Pythonidae Scat application.
        """
        # noinspection PyArgumentEqualDefault
        Logger.set_verbose(True)
        Logger.set_debug(False)

    # noinspection PyUnresolvedReferences,PyMethodMayBeStatic
    def execute(self, settings):
        """
        Execute the tasks specified in the settings object.

        :param settings: the application settings
        :type settings: argparse.Namespace
        :return: None
        :raises: ArgumentError
        """
        Logger.set_verbosity(settings.verbosity)
        if settings.logfile is not None and settings.logfile:
            Logger.add_logger(FileLogger(settings.logfile))

        # noinspection PyUnusedLocal
        with GracefulInterruptHandler() as handler:
            # TODO: implement app here
            pass

        return None
