# coding=utf-8

"""
Herring tasks for publishing ReST files to a wordpress blog.
"""

# noinspection PyUnresolvedReferences
from herring.herring_app import task, namespace
# noinspection PyUnresolvedReferences
from herringlib.project_settings import Project
# noinspection PyUnresolvedReferences
from herringlib.local_shell import LocalShell

__docformat__ = 'restructuredtext en'

with namespace('blog'):

    @task()
    def init():
        """establish connection with wordpress blog"""
        with LocalShell() as local:
            local.run('restblog init "{name}" "{url}/xmlrpc.php" {user}'.format(name=Project.blog_name,
                                                                                url=Project.blog_url,
                                                                                user=Project.blog_user))

    @task()
    def create():
        """create a new article"""
        pass

    @task()
    def post():
        """send changed articles to wordpress blog"""
        pass

    @task()
    def fetch():
        """fetch articles from wordpress blog"""
