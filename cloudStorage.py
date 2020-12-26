import dropbox

class TransferData (object): 
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open (file_from, 'rb')
        dbx.files_upload(f.read(), file_to)   

def main ():
    access_token = 'sl.AoK6Wk8ckhFJwvy6Yt12PGIwMbVf7kG0-nwFq1K-OyWQKwkpbRUiIOCQfwr-Ig8ZPQWtNzfY_fZUNlZuXbv127MzmFj14C9Koa0_UZqtRAVVIAt4rzI3LtZWz-XxaTq20oBw4p0'
    transferData1 = TransferData(access_token)
    file_from = input("enter the file name to transfer: ")
    file_to = input ("enter the full path to upload: ")
    transferData1.upload_files(file_from, file_to)
    print ("the file has been stored")

main()    