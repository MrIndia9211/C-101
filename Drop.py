from os import access
import dropbox

class TransferData:
    def __init__(self,access_token) :
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():   
     access_token ='sl.A4x2DqbGaipcB4Kh_Ug30TyzPXD5W38_2RLkwXnIowQ9GpyRu9Ju_4lJkdprVrV1Swf_HrNGlvRGGHWeo3QeA23fbNnU5tZUGTu_NzzSRh1DyMMIQrAeJsIYonz6DJQ7BPpwaPt7v6Y'
     transferData = TransferData(access_token)

     file_from = input('Enter The file path to transfer :-')
     file_to = input('Enter the path to upload to drop box :-')
     
     transferData.upload_file(file_from,file_to)
     print('file has been moved ')

main()


