from remotezip import RemoteZip
class remote_zip_fs_wrapper:
  def __init__(self, zip_url,debug=0):
    set_zip(zip_url,debug)
  def zip_info_list(zip_url):
    with RemoteZip(zip_url) as zip:
      infolist=zip.infolist()
      filelist=zip.filelist()
      zip.close()
      return infolist,filelist
  def zip_extract_file(file_path):
    self.zip.extract(file_path)
  def zip_extract_file(zip_url,file_path):
    with RemoteZip(zip_url) as zip:
      zip.extract(file_path)
      zip.close()
  def zip_open_file(file_path):
     with self.zip.open(file_path) as zip_open_file:
        return zip_open_file.read()
  def zip_open_file(zip_url,file_path):
    with RemoteZip(zip_url) as zip:
      with self.zip.open(file_path) as zip_open_file:
        fileread=zip_open_file.read()
        zip_open_file.close()
        zip.close()
        return fileread()
  def set_zip(zip_url):
    self.zip_url=zip_url
    with RemoteZip(zip_url) as zip:
      self.zip =zip
      self.zip.debug=debug
      self.infolist=zip.infolist()
      self.filelist=zip.filelist()
  def get_zip():
    return self.zip_url,self.zip,self.infolist,self.filelist
