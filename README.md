# FreezeFrame

## Overview

**FreezeFrame** is a Python-based tool designed to enhance video playback by optimizing frame rates and resolution settings on Windows-based systems. By adjusting these parameters, the tool ensures smoother video playback and improved visual quality.

## Features

- Adjusts video frame rate to a target value.
- Resizes video resolution to a specified setting.
- Utilizes OpenCV for video processing.
- Outputs optimized videos in a user-specified format.

## Requirements

- Python 3.x
- OpenCV
- Numpy

You can install the required Python packages using pip:

```bash
pip install opencv-python numpy
```

## Usage

1. **Set up your environment**: Ensure you have Python and the required packages installed.

2. **Prepare your video**: Ensure you have the video file you wish to optimize.

3. **Run FreezeFrame**: 

```bash
python freeze_frame.py
```

4. **Output**: The optimized video will be saved to the specified output path.

## Parameters

- `video_path`: Path to the input video file.
- `target_frame_rate`: Desired frame rate for the output video (default is 30 FPS).
- `target_resolution`: Tuple for the desired resolution, e.g., (1280, 720).

## Example

To optimize a video called `input_video.mp4` and save the output as `output_video.mp4`:

```python
video_path = "input_video.mp4"
output_path = "output_video.mp4"
freeze_frame = FreezeFrame(video_path)
freeze_frame.optimize_video(output_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to contribute to this project.