!pip install remotezip
from remotezip import RemoteZip
with RemoteZip("https://s3.eu-central-1.amazonaws.com/avg-kitti/data_odometry_velodyne.zip") as zip:
    zip.extract('dataset/sequences/21/velodyne/000437.bin')
    for zip_info in zip.infolist():
        print(zip_info.filename)
