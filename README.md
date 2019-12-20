# mwdn-test
Project for MWDN

1. Endpoints:
* / - form for documents upload
* /api/documents/upload/ - API endpoint for documents upload
* /api/documents/ - list of all documents
* /api/documents/{ID}/ - single document
* /api/urls/ - list of all urls

> For every URL, hold an indication whether the URL is “alive”, that is, it will be false
if, for example, a HTTP 4XX status returns when requesting the URL.

Actually it's a bad idea to check urls on the fly during file processing or during api response, I fulfilled this condition only because the task required it. I've chosen second variant. 
