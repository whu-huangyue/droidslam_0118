#coding=utf-8
import os
import time

commands = []

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220215_canteen_night/stereo-frame_left-image_raw' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220215_canteen_night/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220215_garden_night/stereo-frame_left-image_raw_new' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220215_garden_night/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_corridor_day/stereo-frame_left-image_raw_new' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220216_corridor_day/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_escalator_day/stereo-frame_left-image_raw_new' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220216_escalator_day/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220216_MCR_fast/stereo-frame_left-image_raw' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220216_MCR_fast/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/FP/20220226_campus_road_day/stereo-frame_left-image_raw_new' --calib='/home/hy/DROID-SLAM/calib/FP.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/FusionPortable/20220226_campus_road_day/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/00/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/00/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/01/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/01/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/02/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/02/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/03/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti03.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/03/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/04/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/04/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/05/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/05/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/06/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/06/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/07/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/07/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/08/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/08/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/09/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/09/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/Xuhui-Database1/Datasets/SLAM/KITTI/data_odometry_gray/dataset/sequences/10/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI/10/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq01/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq01/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq02/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq02/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq03/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti00-02.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq03/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq04/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq04/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq05/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq05/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/kitti-syn/seq06/image_0' --calib='/home/hy/DROID-SLAM/calib/kitti04-12.txt' --disable_vis""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/KITTI-syn/seq06/trajectory.txt""")

for i in range(len(commands)):
    cur_command = commands[i]
    print(cur_command)
    os.system(cur_command)
    time.sleep(2)