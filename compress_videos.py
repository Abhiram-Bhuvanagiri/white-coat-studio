import os
from moviepy import VideoFileClip

input_dir = 'assets/videos'
output_dir = 'assets/videos_compressed'
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 8):
    input_file = os.path.join(input_dir, f'vid-{i}.mp4')
    output_file = os.path.join(output_dir, f'vid-{i}.mp4')
    
    print(f"Compressing {input_file}...")
    try:
        # Load the clip
        clip = VideoFileClip(input_file)
        
        # We know the CSS card is 250x444. Let's scale down to height=480.
        # This reduces decoding load massively while keeping it perfectly sharp for the container.
        clip_resized = clip.resized(height=480)
        
        # Write the compressed video
        clip_resized.write_videofile(
            output_file, 
            codec='libx264',
            audio=False, # The CSS says muted, we can strip audio to save even more space/decoding
            bitrate="500k",
            preset="fast"
        )
        print(f"Successfully compressed to {output_file}")
    except Exception as e:
        print(f"Failed to compress {input_file}: {e}")
