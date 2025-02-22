# FrameWise
An AI-powered photography assistant that provides real-time voice-guided posing instructions and automated capturing using a smartphone’s back camera, ensuring well-composed shots without a photographer.

![Screenshot 2025-02-22 at 10 02 03 AM](https://github.com/user-attachments/assets/ce47f354-142b-495b-aa38-c1a1a363c811)

FrameWise is an AI-powered photography assistant that provides real-time pose guidance and automated capturing using a smartphone’s back camera. The system leverages computer vision and machine learning to analyze user posture, providing voice-guided adjustments for optimized framing before capturing an image.

The mobile application is developed using CapacitorJS and Svelte, ensuring a lightweight, cross-platform experience. Camera handling is managed via MediaStream APIs (Web). A companion app, synchronized using d WebSockets for real-time live preview and setting adjustments, enables remote control over the same network.

AI processing follows a hybrid local-cloud strategy for optimal performance. On-device processing utilizes MediaPipe for pose estimation, MoveNet for body tracking, and Android Text-to-Speech (TTS) for voice feedback. For lower-end devices, the system dynamically switches to cloud-based AI processing, executed via a FastAPI backend on a GPU server, requiring user authentication.

The backend, implemented in Go, manages application logic, with PostgreSQL for handling user data, preferences, and authentication. A built-in benchmarking system evaluates device capabilities, automatically toggling between local and cloud-based AI for efficiency.

FrameWise ensures low-latency, AI-optimized photography automation, making it ideal for solo users, content creators, and professionals needing high-quality, self-directed shots without external assistance.

[FOSSHack Project](https://fossunited.org/hack/fosshack25/p/8ookaq60g0)


