import argparse
from capture import FrameCapture

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video stream output from the camera')
    parser.add_argument('address',
                        type=int,
                        help='enter camera address')
    args = parser.parse_args()
    stream = FrameCapture(args.address)
    stream.connect()
    print('Press "Escape" to stop stream')
    stream.display_stream()
