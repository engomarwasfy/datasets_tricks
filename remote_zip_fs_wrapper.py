!pip install remotezip
from remotezip import RemoteZip
class remote_zip_fs_wrapper:
  zip_url=None
  zip=None
  infolist=[]
  filelist=[]
  def set_zip(self,zip_url,debug):
    self.zip_url=zip_url
    with RemoteZip(zip_url) as zip:
      self.zip =zip
      self.zip.debug=debug
      self.infolist=zip.infolist()
      self.filelist=[]
      for zip_info in zip.infolist():
        self.filelist.append(zip_info.filename)
  def __init__(self, zip_url,debug):
    self.set_zip(zip_url,debug)
  def tmp_zip_info_list(self,zip_url):
    with RemoteZip(zip_url) as zip:
      infolist=zip.infolist()
      filelist=[]
      for zip_info in zip.infolist():
        filelist.append(zip_info.filename)
      return infolist,filelist
  def tmp_zip_extract_file(self,zip_url,file_path):
    with RemoteZip(zip_url) as zip:
      zip.extract(file_path)
  def zip_extract_file(self,file_path):
    self.tmp_zip_extract_file(self.zip_url,file_path)
  def tmp_zip_open_file(self,zip_url,file_path):
    with RemoteZip(zip_url) as zip:
      with zip.open(file_path) as zip_open_file:
        fileread=zip_open_file.read()
        return fileread
  def zip_open_file(self,file_path):
     self.tmp_zip_open_file(self.zip_url,file_path)
  def get_zip(self):
    return self.zip_url,self.zip,self.infolist,self.filelist
  def close_zip(self):
    self.zip.close()
