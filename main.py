import numpy as np
import argparse
import os
from utils import Model

def main():
    # Main Function
    
    root_dir = f'./plots/{args.data}/'
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Load Data
    model = Model(root_dir)
    model.load_IMUData(f'../data/Imu{args.data}.npz')
    model.load_EncoderData(f'../data/Encoders{args.data}.npz')
    model.set_init(args.init_pos)
    model.motion_model(plot = args.show)
    print('Odometry Done')
    model.load_LidarData(f'../data/Hokuyo{args.data}.npz')
    model.scanMatch(args.show)
    print('Scan Matching Done')
    model.occupancy_map(f"../data/Kinect{args.data}.npz", args.data, saved = args.saved, show = args.show)
    print('Occupancy Map Created')
    model.factorgraph(f"../data/Kinect{args.data}.npz", args.data,saved = args.saved, show = args.show, close = False)
    print('Factor Graph Done')
    model.factorgraph(f"../data/Kinect{args.data}.npz", args.data ,saved = args.saved, show = args.show,close = True)
    print('Closed Graph Done')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=int, default=20, help='Dataset Number')
    parser.add_argument('--init_pos', type=float, nargs='*', help = 'Initial postion of robot, set as identity in the beginning')
    parser.add_argument('--show', action = 'store_true', help = 'Show Results')
    parser.add_argument('--saved', action = 'store_true', help = 'Load saved Results')
    
    args = parser.parse_args()
    main()
    