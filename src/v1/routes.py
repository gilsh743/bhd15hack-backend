# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.nms_document_attachment_raw_attachment_id import NmsDocumentAttachmentRawAttachmentId
from .api.nms_document_raw_document_id import NmsDocumentRawDocumentId


routes = [
    dict(resource=NmsDocumentAttachmentRawAttachmentId, urls=['/nms/document/attachment/raw/<attachment_id>'], endpoint='nms_document_attachment_raw_attachment_id'),
    dict(resource=NmsDocumentRawDocumentId, urls=['/nms/document/raw/<document_id>'], endpoint='nms_document_raw_document_id'),
]