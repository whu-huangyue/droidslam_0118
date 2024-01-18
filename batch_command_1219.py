#coding=utf-8
import os
import time

commands = []

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence34/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq34/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence35/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq35/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence36/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq36/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence37/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq37/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence38/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq38/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence39/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq39/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence40/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq40/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence41/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq41/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence42/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq42/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence43/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq43/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence44/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq44/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence45/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq45/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence46/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq46/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence47/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq47/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence48/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq48/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence49/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq49/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence50/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq50/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence51/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq51/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence52/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq52/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence53/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq53/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence54/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq54/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence55/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq55/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence56/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq56/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence57/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq57/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence58/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq58/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence59/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq59/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC_Syn/Sequence60/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC-syn/seq60/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/MH_01_easy/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/mh01/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/MH_02_easy/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/mh02/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/MH_03_medium/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/mh03/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/MH_04_difficult/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/mh04/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/MH_05_difficult/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/mh05/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V1_01_easy/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v11/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V1_02_medium/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v12/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V1_03_difficult/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v13/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V2_01_easy/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v21/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V2_02_medium/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v22/trajectory.txt""")

commands.append("""python '/home/hy/下载/demo.py' --imagedir='/media/hy/B0CC6321622802A9/ORB-Exp/EuRoC/V2_03_difficult/mav0/cam0/data' --calib='/home/hy/DROID-SLAM/calib/euroc.txt' --disable_vis""")
commands.append("""cp ~/DROID-SLAM/trajectory.txt ~/droid_stereo/EuRoC/v23/trajectory.txt""")

for i in range(len(commands)):
    cur_command = commands[i]
    print(cur_command)
    os.system(cur_command)
    time.sleep(2)