def fuse_detections(vision_result, audio_result):
    """
    Simple fusion logic: Return True if both vision and audio indicate presence.
    """
    if vision_result and audio_result:
        return True
    return False