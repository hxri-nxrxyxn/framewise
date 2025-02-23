# 📸 FrameWise - Smart Poses, Perfect Shots 🌟

An AI-powered photography assistant that provides real-time voice-guided posing instructions 🗣️ and automated capturing 🤖 using a smartphone’s back camera 📱, ensuring well-composed shots 🖼️ without a photographer.


## ℹ️ Project Overview

![Screenshot 2025-02-22 at 10 02 03 AM](https://github.com/user-attachments/assets/ce47f354-142b-495b-aa38-c1a1a363c811)

![image](https://github.com/user-attachments/assets/02b4a895-9fef-4046-8725-b99800f3a3ff)

![image](https://github.com/user-attachments/assets/5709702b-3385-4bcd-bee2-51dab429beac)



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

3.  **Install `cloudflared`:**

    * Follow the installation instructions for your operating system from the official Cloudflare documentation: [https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/)

2.  **Authenticate `cloudflared`:**

    ```bash
    cloudflared tunnel login
    ```

    This will open a browser window for authentication.

4.  **Run the Go Server:**

    ```bash
    cd goapi && go run main.go
    ```

    This will start your Go server on port 8080.

5.  **Run the Python Server:**

    ```bash
    cd fastapi && python3 main.py
    ```

    This will start your Python server on a default port. Note the port number.

6.  **Run the Node.js Development Server:**

    ```bash
    npm run dev
    ```

    This will start your Node.js development server.

7.  **Create Cloudflare Tunnels:**

    * **For the Go server (8080):**

        ```bash
        cloudflared tunnel run --url localhost:8080
        ```

        This will output a `trycloudflare.com` URL (e.g., `https://random-string.trycloudflare.com`). Note this URL.

    * **For the Python server (replace `<python_port>` with the actual port):**

        ```bash
        cloudflared tunnel run --url localhost:<python_port>
        ```

        This will output another `trycloudflare.com` URL. Note this URL.

8.  **Update Application Configuration:**

    * Replace the following in your application's configuration:
        * `baseUrl`: The `trycloudflare.com` URL from the Go server tunnel, appended with `/api/v1` (e.g., `https://random-string.trycloudflare.com/api/v1`).
        * `socketUrl`: The `trycloudflare.com` URL from the Python server tunnel, appended with `/ws` if it is a websocket (e.g., `wss://another-random-string.trycloudflare.com/ws`).

    **Example:**

    ```javascript
    const baseUrl = "[https://random-string.trycloudflare.com/api/v1](https://random-string.trycloudflare.com/api/v1)";
    const socketUrl = "wss://[another-random-string.trycloudflare.com/ws](https://www.google.com/search?q=https://another-random-string.trycloudflare.com/ws)";
    ```
* The configuration is located at `src/script.js`
* These `trycloudflare.com` URLs are temporary.

9.  **Deploy to an Android device or emulator:**
    * Ensure you have Android Studio and the Android SDK installed and configured.
    * Enable wireless debugging on your Android device or start an Android emulator.
    * Connect your device via wireless debugging, or use a running emulator.
    * Run the following command:
      
        ```bash
        npm run and
        ```
    * This will build and deploy the application to your connected Android device or emulator.


## 🧭 Navigating Around
```
.
├── LICENSE
├── README.md
├── capacitor.config.json
├── fastapi
│   └── main.py
├── goapi
│   ├── controller
│   │   └── UserFunctions.go
│   ├── database
│   │   └── postgres.go
│   ├── go.mod
│   ├── go.sum
│   ├── main.go
│   ├── models
│   │   └── User.go
│   └── routes
│       └── UserRoutes.go
├── jsconfig.json
├── ml
│   ├── data_collect_script.py
│   ├── data_process_with_modeltrain.py
│   ├── data_structure.py
│   ├── detection_test.py
│   ├── model_pose1.jpg
│   ├── model_pose2.jpg
│   ├── model_pose3.jpg
│   ├── pose_collect_script.py
│   └── virtual_cameraman_model.h5
├── package-lock.json
├── package.json
├── src
│   ├── app.css
│   ├── app.html
│   ├── lib
│   │   └── Nav.svelte
│   ├── routes
│   │   ├── +layout.svelte
│   │   ├── +page.js
│   │   ├── +page.svelte
│   │   ├── camera
│   │   │   └── +page.svelte
│   │   ├── home
│   │   │   └── +page.svelte
│   │   ├── login
│   │   │   └── +page.svelte
│   │   └── signup
│   │       └── +page.svelte
│   └── script.js
├── static
│   ├── favicon.png
│   ├── lock.svg
│   ├── login.svg
│   ├── photoshoot.svg
│   └── welcome.svg
├── svelte.config.js
├── tree
└── vite.config.js

```
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

## ℹ️ Other Important Diagrams

### Tech Stack
![photo_2025-02-23 16 28 03-modified](https://github.com/user-attachments/assets/73c27ed5-b10f-40c7-9cdf-fbb57e6a5edc)

### Activity Diagram
![photo_2025-02-23 16 27 53-modified](https://github.com/user-attachments/assets/17979f9d-72b4-4647-9b57-2c00682045ed)

## Built for FOSSHack 2025  

Find our [FOSSHack Project](https://fossunited.org/hack/fosshack25/p/8ookaq60g0)

[![FOSSHACK 25 Banner-modified](https://github.com/user-attachments/assets/14de9b30-763b-4bd6-8a03-d2dcab1bf3af)](https://fossunited.org/hack/fosshack25/p/8ookaq60g0)
