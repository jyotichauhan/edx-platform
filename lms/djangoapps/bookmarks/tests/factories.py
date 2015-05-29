"""
Factories for Bookmark models.
"""

import factory
from factory.django import DjangoModelFactory
from functools import partial

from student.tests.factories import UserFactory
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from ..models import Bookmark, XBlockCache

COURSE_KEY = SlashSeparatedCourseKey(u'edX', u'test_course', u'test')
LOCATION = partial(COURSE_KEY.make_usage_key, u'problem')


class BookmarkFactory(DjangoModelFactory):
    """ Simple factory class for generating Bookmark """
    FACTORY_FOR = Bookmark

    user = factory.SubFactory(UserFactory)
    course_key = COURSE_KEY
    usage_key = LOCATION('usage_id')
    path = list()
    xblock_cache = factory.SubFactory(
        'bookmarks.tests.factories.XBlockCacheFactory',
        course_key=factory.SelfAttribute('..course_key'),
        usage_key=factory.SelfAttribute('..usage_key'),
    )


class XBlockCacheFactory(DjangoModelFactory):
    """ Simple factory class for generating XblockCache. """
    FACTORY_FOR = XBlockCache

    course_key = COURSE_KEY
    usage_key = factory.Sequence(u'4x://edx/100/block/{0}'.format)
    display_name = ''
    paths = list()