# mos_sim_demo

## 打包

先在pybullet库的安装位置找到`plane.urdf`和`plane100.obj`，复制到`./urdf/urdf/`文件夹下。然后运行：
```
pyinstaller --add-data ".\urdf;urdf" --add-data ".\ball_image.jpg;." --paths=./walking .\sim_demo.py
```
在打包后，将上面提到的文件夹`urdf`和图像文件`ball_image.jpg`复制到和`sim_demo.exe`同一文件夹下。
双击该exe文件即可运行。