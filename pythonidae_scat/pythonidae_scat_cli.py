# coding=utf-8
"""
The command line interface for the Pythonidae Scat application.

"""
__docformat__ = 'restructuredtext en'

from pythonidae_scat.pythonidae_scat_settings import PythonidaeScatSettings
from fullmonty.simple_logger import error, info

__all__ = ("ArgumentError", "Pythonidae ScatCLI")


class ArgumentError(RuntimeError):
    """There is a problem with a command line argument"""
    pass


class PythonidaeScatCLI(object):
    """
    Command Line Interface for the Pythonidae Scat App
    """

    def execute(self, app):
        """
        Handle the command line arguments then execute the app.

        :param app: the application instance
        :type app: pythonidae_scat.Pythonidae ScatApp
        """
        with PythonidaeScatSettings() as settings:
            try:
                results = app.execute(settings)
                if results is not None:
                    self.report(results)
                exit(0)
            except ArgumentError as ex:
                error(str(ex))
                exit(1)

    # noinspection PyMethodMayBeStatic
    def report(self, results):
        """

        :param results: (success[], error[], missing_filters_for_rule_ids[])
        :type results: tuple
        """
        # TODO: implement result report
        info("Results: {results}".format(results=repr(results)))
