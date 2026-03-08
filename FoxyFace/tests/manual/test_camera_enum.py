#!/usr/bin/env python3
"""
Simple test script to verify camera enumeration works correctly.
This can be run manually to see what cameras are detected.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from src.stream.camera.CameraEnumerator import CameraEnumerator


def main():
    print("=" * 60)
    print("Camera Enumeration Test")
    print("=" * 60)
    
    print("\nEnumerating cameras...")
    cameras = CameraEnumerator.get_available_cameras()
    
    if not cameras:
        print("No cameras found!")
        return
    
    print(f"\nFound {len(cameras)} camera(s):")
    for camera in cameras:
        print(f"  Index: {camera.index}, Name: {camera.name}")
    
    # Test finding by name
    if cameras:
        test_name = cameras[0].name
        print(f"\nTesting find_camera_by_name with '{test_name}'...")
        found_index = CameraEnumerator.find_camera_by_name(test_name, cameras)
        if found_index is not None:
            print(f"✓ Successfully found camera at index {found_index}")
        else:
            print("✗ Failed to find camera")
    
    print("\n" + "=" * 60)


if __name__ == '__main__':
    main()
