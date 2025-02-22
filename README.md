# 📸 FrameWise - Smart Poses, Perfect Shots 🌟

An AI-powered photography assistant that provides real-time voice-guided posing instructions 🗣️ and automated capturing 🤖 using a smartphone’s back camera 📱, ensuring well-composed shots 🖼️ without a photographer.


## ℹ️ Project Overview

![Screenshot 2025-02-22 at 10 02 03 AM](https://github.com/user-attachments/assets/ce47f354-142b-495b-aa38-c1a1a363c811)

FrameWise is an AI-powered photography assistant that provides real-time pose guidance and automated capturing using a smartphone’s back camera. The system leverages computer vision and machine learning to analyze user posture, providing voice-guided adjustments for optimized framing before capturing an image.

**Key Features:**

* **Real-time Pose Guidance:** Voice-guided adjustments for optimal framing.
* **Automated Capturing:** Hands-free photography using the smartphone's back camera.
* **Hybrid Local-Cloud AI Processing:** Optimizes performance based on device capabilities.
* **Cross-Platform Mobile App:** Developed using CapacitorJS and Svelte.
* **Companion App:** Remote control and live preview via WebSockets.
* **Backend System:** Go-based backend with PostgreSQL for data management.

**Technical Details:**

* **Mobile App:** CapacitorJS, Svelte, MediaStream API (Web).
* **AI Processing:** MediaPipe, MoveNet, Android TTS (local); FastAPI (cloud).
* **Backend:** Go, PostgreSQL.
* **Communication:** WebSockets.

## 🔗 Links

* [CapacitorJS](https://capacitorjs.com/)
* [Svelte](https://svelte.dev/)
* [MediaStream API](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)
* [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
* [MediaPipe](https://google.github.io/mediapipe/)
* [MoveNet](https://www.tensorflow.org/hub/tutorials/movenet)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Go (Golang)](https://golang.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Android Text-to-Speech (TTS)](https://developer.android.com/reference/android/speech/tts/TextToSpeech)

## 🛠️ Getting Started

To get started with FrameWise, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hxri-nxrxyxn/framewise
    cd framewise
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    This will start a development server for testing the application in a web browser.

4.  **Deploy to an Android device or emulator:**
    * Ensure you have Android Studio and the Android SDK installed and configured.
    * Enable wireless debugging on your Android device or start an Android emulator.
    * Connect your device via wireless debugging, or use a running emulator.
    * Run the following command:
      
        ```bash
        npm run and
        ```
    * This will build and deploy the application to your connected Android device or emulator.

## 🤝 Contributing

We welcome contributions to FrameWise! If you'd like to contribute, please follow these guidelines:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3.  **Make your changes** and commit them: `git commit -m 'Add your feature'`.
4.  **Push your changes** to your fork: `git push origin feature/your-feature-name`.
5.  **Submit a pull request** to the `main` branch of the original repository.

Please ensure your code follows the project's coding style and includes appropriate tests.

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Built for FOSSHack 2025  

Find our [FOSSHack Project](https://fossunited.org/hack/fosshack25/p/8ookaq60g0)

[![FOSSHACK 25 Banner-modified](https://github.com/user-attachments/assets/14de9b30-763b-4bd6-8a03-d2dcab1bf3af)](https://fossunited.org/hack/fosshack25/p/8ookaq60g0)
