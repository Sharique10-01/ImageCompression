import os
import ffmpeg
from IPython.display import display, HTML

# Function to compress video with bitrate, CRF, resolution, and FPS
def compress_video_with_bitrate(input_file, crf=30, resolution='1280x720', fps=24, bitrate='1500k', codec='libx264'):
    try:
        # Get the size of the original video before compression
        original_size = os.path.getsize(input_file) / (1024 * 1024)  # Size in MB
        print(f"Original Video Size: {original_size:.2f} MB")
        
        # Create an updated filename with resolution, CRF, FPS, bitrate, and original size
        file_name, file_extension = os.path.splitext(os.path.basename(input_file))
        output_file = f"/content/compressed_{file_name}_FPS_{fps}_resolution_{resolution}_CRF_{crf}_bitrate_{bitrate}_size_{original_size:.2f}MB.mp4"
        
        # Compress the video with CRF, resolution, FPS, and bitrate adjustments, and no audio
        print("Compression started...")
        ffmpeg.input(input_file).output(output_file, vcodec=codec, crf=crf, 
                                        s=resolution, r=fps, video_bitrate=bitrate, an=None).run(capture_stdout=True, capture_stderr=True)
        print(f"Video compression successful: {output_file}")
        
        # Get the size of the compressed video
        compressed_size = os.path.getsize(output_file) / (1024 * 1024)  # Size in MB
        print(f"Compressed Video Size: {compressed_size:.2f} MB")
        
        # Play the compressed video in Colab using HTML5 video embedding
        video_html = f'<video width="640" height="480" controls><source src="/content/{os.path.basename(output_file)}" type="video/mp4"></video>'
        display(HTML(video_html))
        
    except ffmpeg.Error as e:
        print("An error occurred:", e)

# File path of your uploaded video
input_file = '/content/movingFrame.mp4'  # Path to your uploaded video file

# Compress video with updated CRF, resolution, fps, and bitrate
compress_video_with_bitrate(input_file, crf=40, resolution='1280x720', fps=5, bitrate='200k')  # Set the bitrate to 800k
