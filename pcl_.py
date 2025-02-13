import pclpy
from pclpy import pcl

cloud = pcl.Pointcloud.PointXYZ()  # upload dots cloud from file
pcl.io.loadPCDFile(image.pcd)

filter = pcl.filters,VoxelGrid.PointXYZ()
filter.setInputCloud(cloud)
filter.setLeafSize(0.1, 0.1, 0.1)

filtered_cloud = pcl.PointCloud.PointXYZ()
filter.filter(filtered_cloud)

pcl.io.savePCDFile('filtered_point_cloud.pcd', filtered_cloud)  # 

print('Обработка облака точек завершена.')
