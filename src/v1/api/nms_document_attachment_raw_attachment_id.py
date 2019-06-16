# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class NmsDocumentAttachmentRawAttachmentId(Resource):

    def get(self, attachment_id):

        return None, 200, None