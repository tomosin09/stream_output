import argparse
from loguru import logger
from stream import VideoStream

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video stream output from the camera')
    parser.add_argument('--address',
                        default=0,
                        help='enter camera address')
    args = parser.parse_args()
    stream = VideoStream(args.address)
    if stream.is_open():
        while True:
            try:
                stream.show_frame()
            except AttributeError:
                logger.warning(f'failed to reproduce the stream {args.address}')
    else:
        logger.warning(f'stream {args.address} is not available')
    print('Press "Escape" to stop stream')
    stream.display_stream()
