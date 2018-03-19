# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
import logging
logger = logging.getLogger(__name__)
class MainProgram(object):
  def __init__(self):
    try:
        User.objects.create_superuser(username='ibm4',password='bluemix12345',email='ibm4@gmail.com')
    except IntegrityError as e:
        logger.warning("DB Error Thrown %s" % e)
