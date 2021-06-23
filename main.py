import argparse
import time
from loguru import logger
from stream import VideoStream

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video stream output from the camera')
    parser.add_argument('--address',
                        default=0,
                        help='enter camera address')
    args = parser.parse_args()
    stream = VideoStream(args.address)
    logger.info(f'stream resolution is {stream.take_size()}')
    run = True
    if stream.is_open():
        while run:
            try:
                frame = stream.take_frame()
                if frame is None:
                    print('frame empty')
                stream.show_frame()
                # logger.info(f'frame position is {stream.take_pos()}')
            except AttributeError:
                logger.warning(f'failed to reproduce the stream {args.address}')
                run = False
    else:
        logger.warning(f'stream {args.address} is not available')
    print('Press "Escape" to stop stream')
    stream.display_stream()
