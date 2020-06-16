# Welcome to Trello-report-by-python github

## trello_attachment_downloader.py
* bulkdownloads all attachments based on xlsx export list of attachments
### instructions:
 1. export your file to xlsx format with 2 coloumns, [casename, attachments] using TrelloExport Google Chrome Add-on. https://chrome.google.com/webstore/detail/trelloexport/kmmnaeamjfdnbhljpedgfchjbkbomahp?hl=en

 2. place this script and xlsx export file into same folder

 3. requires python 3.7+ and the imported packages.

 4. you can adjust the sleep timer to be shorter than the default .1 seconds to download files faster. but you may run into api-call host rejections if you download too quickly.
