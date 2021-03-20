from moviepy.editor import VideoFileClip, concatenate_videoclips


video_1 = VideoFileClip("WandaVision 1.mp4")
video_2 = VideoFileClip("WandaVision 2.mp4")

final_video= concatenate_videoclips([video_1, video_2])
final_video.write_videofile("WandaVision.mp4")