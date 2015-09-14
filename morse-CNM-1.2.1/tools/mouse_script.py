""" Simple script for the CAT AND MOUSE game tutorial

This will command the CAT, using two semantic cameras, to follow
after the MOUSE robot """

import time
from pymorse import Morse

def main():
    """ Use the semantic cameras to locate the target and follow it """
    with Morse() as morse:
        motion = morse.mouse.m_motion

        while True:
            v_w = {"v": 1.2, "w": 0.3}
            time.sleep(0.5)
            motion.publish(v_w)

if __name__ == "__main__":
    main()
