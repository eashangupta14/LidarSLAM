# Lidar Based SLAM

This is the code for ECE 276A project 2.

In this project, I implemented simultaneous localization and mapping (SLAM) using encoder and IMU odometry, 2-D LiDAR scans, and RGBD measurements from a differential-drive robot. I used the odometry and LiDAR measurements to localize the robot and build a 2-D occupancy grid map of the environment. I use the RGBD images to assign colors to the 2-D map of the floor.

The repo does not contain the icp.py and utils.py file. If required please reach out to me.

<div style="display: flex; justify-content: center; flex-direction: column; align-items: center;">
    <img src="images/example.gif" alt="Example GIF" style="display: block; margin: 0 auto;"  width="300" height="300" />
    <p><em>Figure 1: 2D map made using LIDAR Slam.</em></p>
</div>

## Installation

Follow the steps for setting up the environment  required to run the code on Windows.

```bash
conda create -n <Env Name> python=3.8
conda activate <Env Name>
pip install gtsam
pip install matplotlib
pip install scipy
pip install opencv-python
pip install tqdm
pip install open3d

```

## Folder Structure

This is the folder structure that need to be followed while running the code.

```bash
├───code
│   ├─── plots
│   ├─── main.py
│   ├─── utils.py
│   ├─── icp.py
│   ├─── pr2_utils.py
│   ├─── utils2.py
│   ├─── test_icp.py
│   └───__pycache__
├───code2
│   └───icp_warm_up
│       ├───data
│       │   ├───drill
│       │   │   └───images_for_reference
│       │   └───liq_container
│       │       └───images_for_reference
│       └───__pycache__
├───data
│   ├───dataRGBD
│   │   ├───Disparity20
│   │   ├───Disparity21
│   │   ├───RGB20
│   │   └───RGB21
│   ├───Imu20.npz
└───docs
```

## To Run

Follow the commands to run the program.

### For running main Program

```bash
cd code
python main.py --data <dataset number> --show
```

For example to run dataset 20 use:

```bash
cd code
python main.py --data 20 --show
```

### For ICP warmup

```bash
cd code
python test_icp.py
```

## Results

Results will be shown in form of plots as the code progresses. Close the graphs to continue the code.
Also for main run the graphs will be saved in `plots` folder in the code directory.
