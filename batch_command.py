#coding=utf-8
import os
import time

commands = []

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/XTDrone/Seq005/image_right_new' --calib='/home/hy/DROID-SLAM/calib/XTDrone.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/XTDrone/Seq005/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene003-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene003/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene006-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene006/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene009-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene009/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene052-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene052/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene076-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene076/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene100-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene100/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene106-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene106/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene115-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene115/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene135-1205/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene135/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene137-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene137/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene163-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene163/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene174-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene174/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/scene175-1202/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene175/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene007/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene007/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene048/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene048/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene055/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene055/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene075/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene075/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene080/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene080/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene092/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene092/trajectory.txt""")

# commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene103/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
# commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene103/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/isaac-sim/record/xuhui/Scene165/image_left' --calib='/home/hy/DROID-SLAM/calib/isaac.txt'""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/isaacsim/scene165/trajectory.txt""")

for i in range(len(commands)):
    cur_command = commands[i]
    print(cur_command)
    os.system(cur_command)
    time.sleep(2)
